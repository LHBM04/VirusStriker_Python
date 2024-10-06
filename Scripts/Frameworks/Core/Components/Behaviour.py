from abc import ABCMeta, abstractmethod
from typing import final

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject

class Behaviour(Component, metaclass = ABCMeta):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)
        self.__isEnabled: bool = True

    # [Properties]
    @property
    def isEnabled(self) -> bool:
        return self.__isEnabled

    @isEnabled.setter
    def isEnabled(self, _enable) -> None:
        self.__isEnabled = _enable

    # [Life-Cycle Methods]
    @abstractmethod
    def OnEnabled(self) -> None:
        pass

    @abstractmethod
    def Start(self) -> None:
        pass

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def OnDisable(self) -> None:
        pass

    @abstractmethod
    def OnDestroy(self) -> None:
        pass