from abc import abstractmethod
from typing import Dict, List, final, Union

from pico2d import Image

from Core.Components.Behavior import Behavior
from Core.Components.GameObject import GameObject
from Core.Components.SpriteRenderer import SpriteRenderer
from Core.Utilities.ResourceManagement import ResourceLoader

class Animation:
    def __init__(self,
                 _animator: 'Animator',
                 _isLoop: bool = True):
        self.__animator: 'Animator'             = _animator
        self.__spriteRenderer: SpriteRenderer   = _animator.gameObject.GetComponent(SpriteRenderer)

        self.__isLoop: bool                 = _isLoop   # 해당 스프라이트의 루프 여부.
        self.__isEnd: bool                  = False     # 해당 스프라이트의 루프 종료 여부.
        self.__currentAnimateTime: float    = 0.1       # 해당 스프라이트의 애니메이션 시간.
        self.__animationDeltaTime: float    = 0.0       # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.

        self.__sprites: list[Image]     = []    # 해당 스프라이트의 텍스쳐들
        self.__currentSpriteIndex: int  = 0     # 해당 스프라이트의 현재 텍스쳐.
    # region [Properties]
    @property
    def sprites(self) -> List[Image]:
        return self.__sprites

    @sprites.setter
    def sprites(self, _sprites: Union[str, List[Image]]):
        if isinstance(_sprites, str):
            self.__sprites = ResourceLoader().LoadSprites(_sprites)
        elif isinstance(_sprites, list):
            self.__sprites = _sprites
        else:
            raise ValueError()

    @property
    def spritesLength(self) -> int:
        return len(self.__sprites) if self.__sprites else 0

    @property
    def isLoop(self) -> bool:
        return self.__isLoop

    @isLoop.setter
    def isLoop(self, _loop: bool) -> None:
        self.__isLoop = _loop

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @property
    def currentAnimateTime(self) -> float:
        return self.__currentAnimateTime

    @property
    def animationDeltaTime(self) -> float:
        return self.__animationDeltaTime
    # endregion
    @abstractmethod
    def Animate(self, _deltaTime: float):
        self.__animationDeltaTime += _deltaTime

        if self.__animationDeltaTime > self.__currentAnimateTime:
            self.__animationDeltaTime -= self.__currentAnimateTime
            self.__currentSpriteIndex += 1

            if self.__currentSpriteIndex >= self.spritesLength:
                if self.isLoop:
                    self.__currentSpriteIndex = 0
                    self.__isEnd = False
                else:
                    self.__currentSpriteIndex = self.spritesLength - 1
                    self.__isEnd = True
                    return  # 종료

            self.__animator.gameObject.GetComponent(SpriteRenderer).sprite = self.__sprites[self.__currentSpriteIndex]

@final
class Animator(Behavior):
    def __init__(self, _actor: GameObject):
        super().__init__(_actor)

        self.__animations: Dict[str, Animation] = {}
        self.__currentAnimation: Animation      = None
        self.__nextAnimation: str               = ""

    def SetState(self, _stateName: str) -> None:
        if _stateName not in self.__animations:
            raise ValueError()

        self.__nextAnimation = _stateName

    def AddAnimation(self, _state: str, _animation: Animation) -> None:
        self.__animations[_state] = _animation

    def Update(self, _deltaTime: float):
        if self.__nextAnimation == "":
            return

        self.__currentAnimation = self.__animations[self.__nextAnimation]
        self.__nextAnimation    = ""

    def LateUpdate(self, _deltaTime: float):
        if self.__currentAnimation is None:
            return

        self.__currentAnimation.Animate(_deltaTime)
