from Core.Components.GameObject import GameObject
from Core.Components.Collider2D.Collider2D import Collider2D

# 원형 Collider2D (미구현)
class CircleCollider2D(Collider2D):
    def __init__(self, _owner: GameObject, _radius: float) -> None:
        super().__init__(_owner)
        self.radius: float = _radius

    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass
