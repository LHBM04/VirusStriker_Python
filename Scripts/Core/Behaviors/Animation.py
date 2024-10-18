from typing import Dict

from Core.Behaviors.Behavior import Behavior

class Animation:
    pass

class Animator(Behavior):
    def __init__(self, _actor: 'GameObject'):
        super().__init__(_actor)

        self.__animation: Dict[str, Animation] = {};
        self.__animationDeltaTime: float = 0;
        self.__animationDeltaTime

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
