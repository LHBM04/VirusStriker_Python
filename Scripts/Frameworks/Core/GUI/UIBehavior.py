from abc import ABCMeta

from Core.Components.Behaviour import Behavior
from Core.Components.GameObject import GameObject

class UIBehavior(Behavior, metaclass = ABCMeta):
    def __init__(self, _uiObject: GameObject):
        super().__init__(_uiObject)

