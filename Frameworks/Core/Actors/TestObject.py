from Core.System import *
from Core.Actors.Object import *
from Core.Actors.CollisionSystem import *
from Core.Actors.CollisionSystem import Collider2D
from Level.LevelManagement import *
from Utilities.InputManagement import *

class TestPlayer(Object):
    def __init__(self) -> None:
        super().__init__()

        self.position = Vector2(640, 400)

        self.sprite = Sprite("Resources/Sprites/Objects/Actors/Player/Idle")
        self.spriteInfo = SpriteInfo(_position = Vector2(640, 400), 
                                     _scale = Vector2(100, 100),
                                     _rotate = 0.0,
                                     _isFlipX = False,
                                     _isFlipY = False,
                                     _color = Color(255, 255, 255, 255))
        self.renderLayer = 1 
        
        self.collisionLayer = 1
        self.colisionTag = Collider2D.ETag.NONE
        self.bodies.append(Collider2D(self, Vector2(0, 0), Vector2(5, 5)))
        
        self.moveDirection: Vector2 = Vector2()
        self.moveSpeed: float = 30.0
        
    def Update(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_w) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Up() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyState(SDLK_s) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Down() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyState(SDLK_a) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Left() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyState(SDLK_d) == EInputState.PRESS:
            self.moveDirection = self.moveDirection + Vector2.Right() * (self.moveSpeed * _deltaTime)

        self.position += self.moveDirection
        self.moveDirection = Vector2()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass
    
    def LateUpdate(self, _deltaTime: float) -> None:
        pass
    
    def OnCollision(self, _colider: Collider2D) -> None:
        return super().OnCollsion(_colider)

    def OnTrigger(self, _colider: Collider2D) -> None:
        return super().OnTrigger(_colider)

    def Render(self) -> None:
        self.spriteInfo.position = self.position
        self.sprite.Render(self.spriteInfo)
    
    def RenderDebug(self) -> None:
        pass
        