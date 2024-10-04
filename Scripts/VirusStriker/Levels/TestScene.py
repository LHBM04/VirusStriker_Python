from typing import final

from pico2d import *

from Core.System import SystemManager
from Core.Utilities.InputManagement import InputManager
from Core.Utilities.ResourceManagement import ResourceManager
from Level.SceneManagement.SceneManager import Scene

@final
class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.testBGM: Music   = ResourceManager().GetBGM(r"Resources\Audio\BGM\BGM_Title.wav")
        self.testSFX: Wav     = ResourceManager().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.wav")

    def OnEnter(self) -> None:
        print("Hello, World!")

        self.testBGM.set_volume(17)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        print("Update")
        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(15)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        print("Fixed Update")

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()