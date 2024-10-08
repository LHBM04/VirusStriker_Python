from typing import final

from pico2d import *

from Core.Components.GameObject import GameObject
from Core.GUI.Text import Text
from Core.SystemManagement import SystemManager
from Core.Utilities.InputManagement import InputManager
from Core.Utilities.Mathematics import Vector2
from Core.Utilities.ResourceManagement import ResourceLoader
from Level.SceneManagement import Scene

@final
class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.testBGM: Music   = ResourceLoader().GetBGM(r"Resources\Audio\BGM\BGM_Title.flac")
        self.testSFX: Wav     = ResourceLoader().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.flac")

        self.testUI: GameObject             = GameObject()
        self.testUI.transform.position      = Vector2(SystemManager().windowWidth / 2, SystemManager().windowHeight / 2)
        self.testText: Text                 = self.testUI.AddComponent(Text)
        self.testText.font                  = ResourceLoader().GetFont(r"Resources\Fonts\BMDOHYEON_otf.otf")
        self.testText.text                  = "Hello, World!"

    def OnEnter(self) -> None:
        super().OnEnter()

        self.testText.Render()
        self.testBGM.set_volume(50)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        super().OnUpdate(_deltaTime)

        self.testText.Render()
        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(7)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        super().OnFixedUpdate(_fixedDeltaTime)

    def OnExit(self) -> None:
        super().OnExit()

    def OnRenderObject(self) -> None:
        super().OnRenderObject()

    def OnRenderGUI(self) -> None:
        super().OnRenderGUI()