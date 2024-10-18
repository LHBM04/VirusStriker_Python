from typing import Dict

from Core.Behaviors.Behavior import Behavior

class Animation:
    """
    각종 오브젝트의 애니메이션을 구현합니다.
    """
    def __init__(self):
        self.__isLoop: bool = False     # 애니메이션 루프 여부.
        self.__isEnd: bool  = False     # 애니메이션 종료 여부.

    @property
    def isLoop(self) -> bool:
        return self.__isLoop

    @isLoop.setter
    def isLoop(self, _value: bool) -> None:
        self.__isLoop = _value

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

class Animator(Behavior):
    """
    애니메이션을 관리하고 재생합니다.
    """
    def __init__(self, _actor: 'GameObject'):
        super().__init__(_actor)

        self.__animations: Dict[str, Animation]     = {}    # 관리 중인 애니메이션들.
        self.__animationDeltaTime: float            = 0.1   # 애니메이션 제어 시간.
        self.__currentDeltaTime: float              = 0.0   # 현재 진행된 애니메이션 시간.

    def Start(self):
        pass

    def OnEnable(self) -> None:
        pass

    def Update(self, _deltaTime: float):
        pass

    def FixedUpdate(self, _fixedDeltaTime: float):
        pass

    def LateUpdate(self, _deltaTime: float):
        pass

    def OnDisable(self) -> None:
        pass

    def OnDestroy(self):
        pass
