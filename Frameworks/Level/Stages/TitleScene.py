from pico2d import *

from Frameworks.Core.Sprite import *
from Frameworks.Core.Utilities.Mathematics.Vector2 import *
from Frameworks.Core.Utilities.InputManagement.InputManager import *
from Frameworks.Level.Scene import *

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        self.m_titleBackground: Sprite = Sprite("Resources\\Sprites\\Backgrounds\\Title\\Main Title")
        self.m_titleBackground.info.position = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.m_titleBackground.info.scale = Vector2(get_canvas_width(), get_canvas_height())
        self.m_titleBackground.info.color = Color(255, 255, 255, 255)
        self.m_titleBackground.isLoop = True
        self.m_titleBackground.info.layerLevel = ELayerLevel.BACKGROUND
        self.m_titleBackground.info.renderLayer = 0

        self.m_titleLogo: Sprite = Sprite("Resources\\Sprites\\GUI\\Logo")
        self.m_titleLogo.info.position = Vector2(390.0, 525.0)
        self.m_titleLogo.info.scale = Vector2(578 / 1.25, 504 / 1.25)
        self.m_titleLogo.info.color = Color(255, 255, 255, 255)
        self.m_titleLogo.info.layerLevel = ELayerLevel.UI
        self.m_titleLogo.info.renderLayer = 0

        self.m_actionCue: Sprite = Sprite("Resources\\Sprites\\GUI\\Press Any Key")
        self.m_actionCue.info.position = Vector2(375.0, 180.0)
        self.m_actionCue.info.scale = Vector2(600 / 1.5, 90 / 1.5)
        self.m_actionCue.info.color = Color(255, 255, 255, 255)
        self.m_actionCue.info.layerLevel = ELayerLevel.UI
        self.m_actionCue.info.renderLayer = 1

    def OnEnter(self) -> None:
        pass

    def OnUpdate(self, _deltaTime: float) -> None:
        self.m_titleBackground.Update(_deltaTime)

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

        self.m_titleBackground.Render()
        self.m_titleLogo.Render()
        self.m_actionCue.Render()

    def OnUIRender(self) -> None:
        super().OnUIRender()
