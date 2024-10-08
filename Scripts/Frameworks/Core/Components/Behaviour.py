from abc import ABCMeta
from typing import final

from Core.Components.Component import Component

class Behavior(Component, metaclass = ABCMeta):
    def __init__(self, _actor: 'GameObject'):
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

            self.__isEnabled = True
            self.OnEnable()
        else:
            if not self.__isEnabled:
                return

            self.__isEnabled = False
            self.OnDisable()
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