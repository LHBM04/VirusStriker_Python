from abc import abstractmethod
from typing import final

from Core.Components.Behavior import Behavior

class UIBehavior(Behavior):
    @final
    def Update(self, _deltaTime: float):
        self.Render()
        self.RenderDebug()

    @abstractmethod
    def Render(self):
        pass

    @abstractmethod
    def RenderDebug(self):
        pass