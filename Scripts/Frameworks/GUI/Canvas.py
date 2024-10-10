from typing import List

from Core.Components.Behavior import Behavior
from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from GUI.UIBehaivor import UIBehavior

class Canvas(Behavior):
    def __init__(self, _actor: GameObject):
        super().__init__(_actor)

        self.uiBehaviors: List[UIBehavior]    = []
        self.addUIBehaviors: List[UIBehavior] = []

    def Update(self, _deltaTime: float):
        for uiBehavior in self.uiBehaviors:
            uiBehavior.Update(_deltaTime)

class CanvasRenderer(Component):
    pass