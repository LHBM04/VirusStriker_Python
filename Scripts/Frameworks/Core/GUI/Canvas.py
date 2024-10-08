from Core.Components.GameObject import GameObject
from Core.Components.Behaviour import Behavior

class Canvas(Behavior):
    def __init__(self, _uiInterface: GameObject):
        super().__init__(_uiInterface)

