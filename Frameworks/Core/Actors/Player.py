from Core.Actors.Entity import *
from Utilities.InputManagement import *

class Player(Entity):
    def __init__(self) -> None:
        super().__init__()

        self.scale = Vector2(100, 100)

        # 스프라이트 정보
        self.sprite                     = Sprite(self, "Resources\\Sprites\\Objects\\Actors\\Player\\Idle")
        self.sprite.info.layerLevel     = Sprite.Info.ELevel.OBJECT
        self.sprite.info.renderLayer    = 0

        # 콜라이더 정보
        self.collider: Collider2D           = None
        self.collisionTag: Collider2D.ETag  = Collider2D.ETag.NONE
        self.collisionLayer: int            = 0

        self.moveDirection: Vector2 = Vector2()
        self.moveSpeed: float       = 300.0
    
    def Update(self, _deltaTime: float) -> None:
        super().Update(_deltaTime)
        
        if InputManager().GetKeyDown(SDLK_UP):
            self.moveDirection = self.moveDirection + Vector2.Up() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_DOWN):
            self.moveDirection = self.moveDirection + Vector2.Down() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_LEFT):
            self.moveDirection = self.moveDirection + Vector2.Left() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_RIGHT):
            self.moveDirection = self.moveDirection + Vector2.Right() * (self.moveSpeed * _deltaTime)

    def LateUpdate(self, _deltaTime: float) -> None:
        self.position += self.moveDirection
        self.moveDirection = Vector2.Zero()