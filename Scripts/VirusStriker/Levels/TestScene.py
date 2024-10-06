from typing import final

from pico2d import *

from Core.Utilities.InputManagement import InputManager
from Core.Utilities.ResourceManagement.ResourceLoader import ResourceLoader
from Level.SceneManagement.SceneManager import Scene

@final
class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.testBGM: Music   = ResourceLoader().GetBGM(r"Resources\Audio\BGM\BGM_Title.flac")
        self.testSFX: Wav     = ResourceLoader().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.wav")

    def OnEnter(self) -> None:
        super().OnEnter()

        self.testBGM.set_volume(50)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        super().OnUpdate(_deltaTime)

        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(7)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        super().OnFixedUpdate(_fixedDeltaTime)

    def OnExit(self) -> None:
        super().OnExit()

        self.objectManager.ClearObjects()
        self.uiManager.ClearObjects()

    def OnRenderObject(self) -> None:
        super().OnRenderObject()

    def OnRenderGUI(self) -> None:
        super().OnRenderGUI()