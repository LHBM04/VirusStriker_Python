from abc import ABC, abstractmethod
from enum import Enum

from Core.Objects.Actors.Actor import Actor
from Core.Utilities.Mathematics import Vector2

# 충돌 검사를 위한 열거형.
# 필요한 게 있을 때마다 추가하여 쓰도록 하자
class EColliderTag(Enum):
    NONE    = 0  # 더미 태그(기본).
    HARMFUL = 1  # 플레이어에게 해로운 오브젝트의 태그
    LETHAL  = 2  # 플레이어에게 치명적인(즉사) 오브젝트의 태그

# Collider2D 베이스
class Collider2D(ABC):
    def __init__(self, _owner: 'Actor') -> None:
        from Frameworks.Core.Objects.Actors.Actor import Actor

        self.owner: Actor = _owner
        self.tag: EColliderTag = EColliderTag.NONE
        self.useTrigger = False

    @abstractmethod
    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass
    
    @abstractmethod
    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass

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

# 원형 Collider2D
class CircleCollider2D(Collider2D):
    def __init__(self, _owner: Actor, _radius: float) -> None:
        super().__init__(_owner)
        self.radius: float = _radius

    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        # 트리거 상태 검사 (충돌 검사와 비슷하지만 트리거 이벤트 처리 추가)
        if self.IsCollision(_other):
            if not self.isTrigger:
                self.OnTriggerEnter(_other)
            self.isTrigger = True
            self.OnTriggerStay(_other)
        else:
            if self.isTrigger:
                self.OnTriggerExit(_other)
            self.isTrigger = False
