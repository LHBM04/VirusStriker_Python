from typing import final

from pico2d import *

from Core.Utilities.InputManagement import InputManager
from Core.Utilities.ResourceManagement import ResourceManager
from Level.SceneManagement import Scene

@final
class OpeningScene(Scene):
    def __init__(self):
        super().__init__()
        self.testImage = ResourceManager().GetImage(r"Resources\Sprites\Backgrounds\Sprite_Background_Initialize.png")
        self.testBGM = ResourceManager().GetBGM(r"Resources\Audio\BGM\BGM_Title.wav")
        self.testSFX = ResourceManager().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.wav")

    def OnEnter(self) -> None:
        self.testBGM.set_volume(17)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        self.testImage.draw(1280 / 2, 720 / 2)

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