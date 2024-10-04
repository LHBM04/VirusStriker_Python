from abc import ABCMeta, abstractmethod
from enum import Enum

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics.Vector2 import Vector2

# 충돌 검사를 위한 열거형.
# 필요한 게 있을 때마다 추가하여 쓰도록 하자
class EColliderTag(Enum):
    NONE    = 0  # 더미 태그(기본).
    HARMFUL = 1  # 플레이어에게 해로운 오브젝트의 태그
    LETHAL  = 2  # 플레이어에게 치명적인(즉사) 오브젝트의 태그

# Collider2D 베이스
class Collider2D(metaclass = ABCMeta, Component):
    def __init__(self, _owner: GameObject) -> None:
        super().__init__(_owner)

        self.__tag: EColliderTag    = EColliderTag.NONE
        self.__useTrigger           = False

    @property
    def tag(self) -> EColliderTag:
        return self.__tag

    @tag.setter
    def tag(self, _newTag: EColliderTag) -> None:
        self.__tag = _newTag

    @property
    def useTrigger(self) -> bool:
        return self.__useTrigger

    @useTrigger.setter
    def useTrigger(self, _useTrigger: bool):
        self.__useTrigger = _useTrigger

    @abstractmethod
    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass
    
    @abstractmethod
    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass

class BoxCollider2D(Collider2D):
    def __init__(self,
                 _owner: GameObject,
                 _min: Vector2,
                 _max: Vector2) -> None:
        super().__init__(_owner)

        self.min: Vector2 = _min
        self.max: Vector2 = _max

    def IsCollision(self, _other: 'Collider2D') -> bool:
        if not isinstance(_other, BoxCollider2D):
            return False

        # AABB 검사
        min1: Vector2 = self.owner.transform.position + self.min
        min2: Vector2 = _other.owner.transform.position + _other.min
        max1: Vector2 = self.owner.transform.position + self.max
        max2: Vector2 = _other.owner.transform.position + _other.max

        if (min1.x < max2.x and max1.x > min2.x and
            min1.y < max2.y and max1.y > min2.y):
            return True

        return False

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        # 트리거 상태 검사 (충돌 검사와 비슷하지만 트리거 이벤트 처리 추가)
        if self.IsCollision(_other):
            if not self.__useTrigger:
                return False

        return True

# 원형 Collider2D (미구현)
class CircleCollider2D(Collider2D):
    def __init__(self, _owner: GameObject, _radius: float) -> None:
        super().__init__(_owner)
        self.radius: float = _radius

    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass
