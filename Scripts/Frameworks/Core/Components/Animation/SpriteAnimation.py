from typing import List

from pico2d import *

from Core.Components.Animation.Animation import Animation

class SpriteAnimation(Animation):
    def __init__(self, _sprites: List[Image]):
        super().__init__()

        self.__sprites = _sprites
        self.__spriteSize: int = len(self.__sprites)  # 해당 스프라이트의 텍스쳐 개수.
        self.__currentSpriteIndex: int = 0  # 해당 스프라이트의 현재 텍스쳐.

        self.__isLoop: bool = False  # 해당 스프라이트의 루프 여부.
        self.__isEnd: bool = False  # 해당 스프라이트의 루프 종료 여부.
        self.__animationTime: float = 0.1  # 해당 스프라이트의 애니메이션 시간.
        self.__animationDeltaTime: float = 0.0  # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.

    def Update(self, _deltaTime: float):
        super().Update(_deltaTime)

        self.__animationDeltaTime += _deltaTime

        if self.__animationDeltaTime > self.__animationTime:
            self.__animationDeltaTime -= self.__animationTime
            self.__currentSpriteIndex += 1

            if self.__currentSpriteIndex >= self.__spriteSize:
                if self.__isLoop:
                    self.__currentSpriteIndex = 0
                else:
                    self.__currentSpriteIndex = self.__currentSpriteIndex - 1
                    self.__isEnd = True

    def Render(self):
        pass