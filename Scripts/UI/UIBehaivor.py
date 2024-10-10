from abc import abstractmethod
from typing import final

from Core.Behaviors.Behavior import Behavior

class UIBehavior(Behavior):
    @final
    def Update(self, _deltaTime: float):
        super().Update(_deltaTime)

        self.Render()
        self.RenderDebug()

    @abstractmethod
    def Render(self):
        pass

    @abstractmethod
    def RenderDebug(self):
        pass