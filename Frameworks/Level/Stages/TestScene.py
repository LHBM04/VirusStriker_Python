from typing import final

from pico2d import *

from Core.System import SystemManager
from Core.Utilities.InputManagement import InputManager
from Core.Utilities.ResourceManagement import ResourceManager
from Level.SceneManagement import Scene

@final
class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.testImage: Image = ResourceManager().GetSprite(r"Resources\Sprites\Backgrounds\Sprite_Background_Initialize.png")
        self.testBGM: Music   = ResourceManager().GetBGM(r"Resources\Audio\BGM\BGM_Title.wav")
        self.testSFX: Wav     = ResourceManager().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.wav")

    def OnEnter(self) -> None:
        self.testBGM.set_volume(17)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        self.testImage.draw(SystemManager().windowWidth / 2, SystemManager().windowHeight / 2)

        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(15)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()