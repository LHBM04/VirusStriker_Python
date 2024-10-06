from typing import final

from pico2d import *

from Core.Components.Objects.GameObject import GameObject
from Core.System import SystemManager
from Core.Utilities.InputManagement import InputManager
from Core.Utilities.Mathematics.Vector2 import Vector2
from Core.Utilities.ResourceManagement import ResourceManager
from Level.SceneManagement.SceneManager import Scene

@final
class TestScene(Scene):
    def __init__(self):
        super().__init__()
        self.testBGM: Music   = ResourceManager().GetBGM(r"Resources\Audio\BGM\BGM_Title.wav")
        self.testSFX: Wav     = ResourceManager().GetSFX(r"Resources\Audio\SFX\SFX_CalculateScore.wav")

    def OnEnter(self) -> None:
        super().OnEnter()
        
        print("Hello, World!")

        self.testBGM.set_volume(17)
        self.testBGM.play(-1)


        self.testObject : GameObject = GameObject()
        self.testObject.spriteRenderer.sprite = ResourceManager().GetSprite("Resources/Sprites/Backgrounds/Sprite_Background_Initialize.png")
        self.testObject.transform.position = Vector2(SystemManager().windowWidth / 2, SystemManager().windowHeight / 2)
        self.objectManager.AddObject(self.testObject)

    def OnUpdate(self, _deltaTime: float) -> None:
        super().OnUpdate()
        
        print("Update")
        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(15)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        super().OnFixedUpdate()
        
        print("Fixed Update")

    def OnExit(self) -> None:
        super().OnExit()

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()