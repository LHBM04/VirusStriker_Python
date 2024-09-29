from Core.System import *
from Core.Object import *
from Level.Scene import *
from Utilities.InputSystem import *

class TestObject(Object):
    def __init__(self) -> None:
        super().__init__()

        self.sprite = Sprite("Resources/Sprites/Objects/Actors/Player/Idle")
        self.spriteInfo = SpriteInfo(_position = Vector2(640, 400), 
                                     _scale = Vector2(100, 100),
                                     _rotate = 0.0,
                                     _isFlipX = False,
                                     _isFlipY = False,
                                     _color = Color(255, 255, 255, 255))
        self.position = Vector2(640, 400)
        self.renderLayer = 1 
        self.moveDirection: Vector2 = Vector2()
        self.moveSpeed: float = 30.0
        
    def Update(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_w) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Up() * (self.moveSpeed * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_s) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Down() * (self.moveSpeed * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_a) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Left() * (self.moveSpeed * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_d) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Right() * (self.moveSpeed * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        self.position += self.moveDirection
        self.moveDirection = Vector2()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass
    
    def LateUpdate(self, _deltaTime: float) -> None:
        pass
    
    def Render(self) -> None:
        self.spriteInfo.position = self.position
        self.sprite.Render(self.spriteInfo)
    
    def RenderDebug(self) -> None:
        pass
        