from operator import truediv
from typing import final

from pico2d import *
from sdl2 import SDLK_RETURN

from Frameworks.Core.Sprite import Sprite, ELayerLevel
from Frameworks.Core.Utilities.InputManagement.InputManager import InputManager
from Frameworks.Core.Utilities.Mathematics.Color import Color
from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2
from Frameworks.Core.Utilities.ResourceManagement.ResourceManager import ResourceManager
from Frameworks.Level.Scene import Scene
from Frameworks.Level.SceneManager import SceneManager


@final
class OpeningScene(Scene):
    def __init__(self):
        super().__init__()

    def OnEnter(self) -> None:
        pass

    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()