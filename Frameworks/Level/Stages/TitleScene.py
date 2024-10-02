from pico2d import *

from Frameworks.Core.Sprite import *
from Frameworks.Core.Utilities.Mathematics.Vector2 import *
from Frameworks.Core.Utilities.InputManagement.InputManager import *
from Frameworks.Core.Utilities.ResourceManagement.ResourceManager import *
from Frameworks.Level.Scene import *

class TitleScene(Scene):
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
