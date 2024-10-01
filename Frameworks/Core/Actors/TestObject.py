from Core.System import *
from Core.Actors.Object import *
from Level.LevelManagement import *
from Utilities.InputManagement import *

class TestPlayer(Object):
    def __init__(self) -> None:
        super().__init__()

        # self.position   = Vector2(640, 400)
        # self.scale      = Vector2(100, 100)

        self.sprite = Sprite(self, "Resources\\Sprites\\Objects\\Actors\\Player\\Idle")
        self.sprite.info.layerLevel = Sprite.Info.ELevel.OBJECT
        self.sprite.info.renderLayer = 0

        self.collider       = BoxCollider2D(self, Vector2(1, 1), Vector2(50, 50))
        self.colisionTag    = Collider2D.ETag.NONE
        self.collisionLayer = 1
        
        self.moveDirection: Vector2 = Vector2()
        self.moveSpeed: float = 300.0
        
    def Update(self, _deltaTime: float) -> None:
        if InputManager().GetKeyDown(SDLK_UP):
            self.moveDirection = self.moveDirection + Vector2.Up() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_DOWN):
            self.moveDirection = self.moveDirection + Vector2.Down() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_LEFT):
            self.moveDirection = self.moveDirection + Vector2.Left() * (self.moveSpeed * _deltaTime)

        if InputManager().GetKeyDown(SDLK_RIGHT):
            self.moveDirection = self.moveDirection + Vector2.Right() * (self.moveSpeed * _deltaTime)

        self.position += self.moveDirection
        self.moveDirection = Vector2()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass
    
    def LateUpdate(self, _deltaTime: float) -> None:
        pass
    
    def OnCollision(self, _collider: Collider2D) -> None:
        print(f"Collided {str(_collider.owner)}")

    def OnTrigger(self, _collider: Collider2D) -> None:
        print(f"Triggred {str(_collider.owner)}")