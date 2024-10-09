from typing import List

from Core.Components.Behavior import Behavior
from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.GUI.UIBehaivor import UIBehavior


class Canvas(Behavior):
    def __init__(self, _actor: GameObject):
        super().__init__(_actor)

        self.__uiBehaviors: List[UIBehavior]    = []
        self.__addUIBehaviors: List[UIBehavior] = []



class CanvasRenderer(Component):
    pass