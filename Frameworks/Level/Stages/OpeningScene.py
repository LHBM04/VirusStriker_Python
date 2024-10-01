from operator import truediv
from typing import final

from pico2d import *
from sdl2 import SDLK_RETURN

from Frameworks.Core.Sprite import Sprite, ELayerLevel
from Frameworks.Core.Utilities.InputManagement.InputManager import InputManager
from Frameworks.Core.Utilities.Mathematics.Color import Color
from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2
from Frameworks.Level.Scene import Scene
from Frameworks.Level.SceneManager import SceneManager


@final
class OpeningScene(Scene):
    def __init__(self):
        super().__init__()

        self.m_openingBackground: Sprite = Sprite("Resources\\Sprites\\Backgrounds\\Title\\Opening")
        self.m_openingBackground.info.position = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.m_openingBackground.info.scale = Vector2(get_canvas_width(), get_canvas_height())
        self.m_openingBackground.info.color = Color(255, 255, 255, 255)
        self.m_openingBackground.info.layerLevel = ELayerLevel.BACKGROUND
        self.m_openingBackground.info.renderLayer = 0
        self.m_openingBackground.isLoop = False

    def OnEnter(self) -> None:
        pass

    def OnUpdate(self, _deltaTime: float) -> None:
        self.m_openingBackground.Update(_deltaTime)
        if self.m_openingBackground.m_currentTextureIndex >= self.m_openingBackground.m_textureSize - 8:
            SceneManager().LoadLevel("Title Scene")
        if InputManager().GetKeyDown(SDLK_RETURN):
            SceneManager().LoadLevel("Title Scene")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()
        self.m_openingBackground.Render()

    def OnUIRender(self) -> None:
        super().OnUIRender()