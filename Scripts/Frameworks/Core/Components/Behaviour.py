from abc import ABCMeta
from typing import final

from Core.Components.Component import Component

class Behavior(Component, metaclass = ABCMeta):
    from Core.Components.GameObject import GameObject
    def __init__(self, _actor: GameObject):
        super().__init__(_actor)

        self.__isEnabled: bool = True

    # region [Properties]
    @property
    def isEnabled(self) -> bool:
        return self.__isEnabled

    @isEnabled.setter
    def isEnabled(self, _enable: bool) -> None:
        if _enable:
            if self.__isEnabled:
                return

            self.OnEnable()
        else:
            if not self.__isEnabled:
                return

            self.OnDisable()

        self.__isEnabled = _enable
    # endregion
    def OnEnable(self) -> None:
        pass

    def OnStart(self) -> None:
        pass

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def Update(self, _deltaTime: float) -> None:
        pass

    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    def OnTriggerEnter2D(self) -> None:
        pass

    def OnTriggerStay2D(self) -> None:
        pass

    def OnTriggerExit2D(self) -> None:
        pass

    def OnCollisionEnter2D(self) -> None:
        pass

    def OnCollisionEixt2D(self) -> None:
        pass

    def OnDisable(self) -> None:
        pass

    def OnDestroy(self) -> None:
        pass
@final
class BehaviorManager:
    def __init__(self):
        pass