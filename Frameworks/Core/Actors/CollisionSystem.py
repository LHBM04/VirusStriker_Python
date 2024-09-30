from enum import Enum

from Core.Actors import Object
from Utilities import Vector2

# AABB형 콜리전 바디
class Collider2D:
    # 충돌 검사를 위한 열거형.
    # 필요한 게 있을 때마다 추가하여 쓰도록 하자
    class ETag(Enum):
        NONE    = 0 # 더미 태그(기본).
        HARMFUL = 1 # 플레이어에게 해로운 오브젝트의 태그
        LETHAL  = 2 # 플레이어에게 치명적인(즉사) 오브젝트의 태그

    def __init__(self, _owner: Object,  _min: Vector2, _max: Vector2) -> None:
        self.owner  = _owner
        self.min    = _min
        self.max    = _max

# 충돌 검사
def IsCollision(_lhs: Collider2D, _rhs: Collider2D) -> bool:
    # AABB 검사
    min1: Vector2 = _lhs.owner.position + _lhs.min
    max1: Vector2 = _lhs.owner.position + _lhs.max
    min2: Vector2 = _rhs.owner.position + _rhs.min
    max2: Vector2 = _rhs.owner.position + _rhs.max

    if (min1.x > max2.x and max1.x > min2.x and 
        min1.y > max2.y and max1.y > min2.y):
        return True

    return False

# TODO: 트리거 판정도 만들기
def IsTrigger(_lhs: Collider2D, _rhs: Collider2D) -> bool:
    pass