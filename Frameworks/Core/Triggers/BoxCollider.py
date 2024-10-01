from Frameworks.Core.Objects.Actors.Actor import Actor
from Frameworks.Core.Triggers.Collider2D import Collider2D
from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2

class BoxCollider2D(Collider2D):
    def __init__(self, _owner: Actor, _min: Vector2, _max: Vector2) -> None:
        super().__init__(_owner)

        self.min: Vector2 = _min
        self.max: Vector2 = _max

    def IsCollision(self, _other: 'Collider2D') -> bool:
        if not isinstance(_other, BoxCollider2D):
            return False

        # AABB 검사
        min1: Vector2 = self.owner.position + self.min
        min2: Vector2 = _other.owner.position + _other.min
        max1: Vector2 = self.owner.position + self.max
        max2: Vector2 = _other.owner.position + _other.max

        if (min1.x < max2.x and max1.x > min2.x and
                min1.y < max2.y and max1.y > min2.y):
            return True

        return False

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        # 트리거 상태 검사 (충돌 검사와 비슷하지만 트리거 이벤트 처리 추가)
        if self.IsCollision(_other):
            if not self.useTrigger:
                return False

        return True