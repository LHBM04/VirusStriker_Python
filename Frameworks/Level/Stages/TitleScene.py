from pico2d import *

from Frameworks.Core.Sprite import *
from Frameworks.Core.Utilities.Mathematics.Vector2 import *
from Frameworks.Core.Utilities.InputManagement.InputManager import *
from Frameworks.Core.Utilities.ResourceManagement.ResourceManager import *
from Frameworks.Level.Scene import *

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

        self.m_titleBackground: Sprite                  = Sprite(ResourceManager().LoadSprites("Resources\\Sprites\\Backgrounds\\Title\\Main Title"))
        self.m_titleBackground.renderInfo.position      = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.m_titleBackground.renderInfo.scale         = Vector2(get_canvas_width(), get_canvas_height())
        self.m_titleBackground.renderInfo.color         = Color(255, 255, 255, 255)
        self.m_titleBackground.isLoop                   = True
        self.m_titleBackground.renderInfo.layerLevel    = ELayerLevel.BACKGROUND
        self.m_titleBackground.renderInfo.renderLayer   = 0

        self.m_titleLogo: Sprite                = Sprite(ResourceManager().LoadSprite("Resources\\Sprites\\GUI\\Logo"))
        self.m_titleLogo.renderInfo.position    = Vector2(390.0, 525.0)
        self.m_titleLogo.renderInfo.scale       = Vector2(578 / 1.25, 504 / 1.25)
        self.m_titleLogo.renderInfo.color       = Color(255, 255, 255, 255)
        self.m_titleLogo.renderInfo.layerLevel  = ELayerLevel.UI
        self.m_titleLogo.renderInfo.renderLayer = 0

        self.m_actionCue: Sprite                = Sprite(ResourceManager().LoadSprite("Resources\\Sprites\\GUI\\Press Any Key"))
        self.m_actionCue.renderInfo.position    = Vector2(375.0, 180.0)
        self.m_actionCue.renderInfo.scale       = Vector2(600 / 1.5, 90 / 1.5)
        self.m_actionCue.renderInfo.color       = Color(255, 255, 255, 255)
        self.m_actionCue.renderInfo.layerLevel  = ELayerLevel.UI
        self.m_actionCue.renderInfo.renderLayer = 1

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
