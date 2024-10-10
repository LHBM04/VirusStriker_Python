from typing import final

from pico2d import *

from Core.Behaviors.Animator import Animator, Animation
from Core.Components.GameObject import GameObject
from Core.Components.SpriteRenderer import SpriteRenderer
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

        self.testObject: GameObject             = GameObject()
        self.testObject.transform.position      = Vector2(SystemManager().windowWidth / 2, SystemManager().windowHeight / 2)
        self.testObject.transform.scale         = Vector2(SystemManager().windowWidth, SystemManager().windowHeight)

        self.testSprite: SpriteRenderer         = self.testObject.AddComponent(SpriteRenderer)
        self.testSprite.sprite                  = ResourceLoader().GetSprite(r"Resources\Sprites\Backgrounds\Sprite_Background_Initialize.png")

        self.testAnimator: Animator             = self.testObject.AddBehavior(Animator)

        self.testAnimation: Animation           = Animation(self.testAnimator)
        self.testAnimation.sprites              = list(ResourceLoader().LoadSprites(r"Resources\Sprites\Backgrounds\Loading"))

        self.testAnimator.AddAnimation("Test", self.testAnimation)
        self.objMng.AddGameObject(self.testObject)

    def OnEnter(self) -> None:
        super().OnEnter()

        self.testAnimator.SetState("Test")

        self.testBGM.set_volume(50)
        self.testBGM.play(-1)

    def OnUpdate(self, _deltaTime: float) -> None:
        super().OnUpdate(_deltaTime)

        if InputManager().GetKeyDown(SDLK_SPACE):
            self.testSFX.set_volume(7)
            self.testSFX.play()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        super().OnFixedUpdate(_fixedDeltaTime)

    def Render(self):
        super().Render()
        self.testSprite.Render()

    def OnExit(self) -> None:
        super().OnExit()