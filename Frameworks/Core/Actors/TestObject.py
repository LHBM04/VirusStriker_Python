from Core.Object import *
from Utilities.InputSystem import *

class TestObject(Object):
    def __init__(self) -> None:
        super().__init__()

        self.sprite = Sprite("Resources/Sprites/Objects/Actors/Player/Idle")
        self.spriteInfo = SpriteInfo()
        self.renderLayer = 1 
        self.moveDirection: Vector2 = Vector2()
        
    def Update(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_w) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Up() * (10.0 * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_s) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Down() * (10.0 * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_a) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Left() * (10.0 * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

        if InputManager().GetKeyState(SDLK_d) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Right() * (10.0 * _deltaTime) # 속도 향상을 위한 스칼라 우선 계산

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.position += self.moveDirection
        self.moveDirection = Vector2()

        print(f"{self.position.m_x} {self.position.m_y}")
    
    def LateUpdate(self, _deltaTime: float) -> None:
        pass
    
    def Render(self) -> None:
        self.spriteInfo.position = self.position
        self.sprite.Render(self.spriteInfo)
    
    def RenderDebug(self) -> None:
        pass
        