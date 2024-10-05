from abc import ABCMeta, abstractmethod

from Core.Components.Component import ComponentManager
from Core.Components.Transform.Transform import Transform


class UIObject(metaclass = ABCMeta):
    def __init__(self):
        self._componentManager = ComponentManager()
        self._componentManager.AddComponent(Transform(self))

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Render(self):
        pass

    @abstractmethod
    def Destroy(self):
        pass