from enum import Enum

from Utilities.Vector2 import *
from Core.Actors.Object import *
from Utilities.MathF import *

# 콜리전 바디
class CollisionBody:
    # 원형 콜라이더
    class Circle:
        def __init__(self, _radius: float) -> None:
            self.radius =  _radius  # 둘레

    # 박스형 콜라이더
    class AABB:
        def __init__(self, _min: Vector2, _max: Vector2) -> None:
            self.min: Vector2 = _min
            self.max: Vector2 = _max

    # 충돌 검사를 위한 열거형.
    # 필요한 게 있을 때마다 추가하여 쓰도록 하자
    class ETag(Enum):
        NONE    = 0 # 더미 태그(기본).
        HARMFUL = 1 # 플레이어에게 해로운 오브젝트의 태그
        LETHAL  = 2 # 플레이어에게 치명적인(즉사) 오브젝트의 태그

    def __init__(self, _owner: Object) -> None:
        self.aabb: CollisionBody.AABB = None
        self.circle: CollisionBody.Circle = None
        self.owner: _owner

# 충돌 검사
def IsCollision(_lhs: CollisionBody, _rhs: CollisionBody) -> bool:
    # Circle 검사
    dp: Vector2 = _lhs.owner.position - _rhs.owner.position
    dl: float   = MathF.Magnitude(dp)

    if dl < _lhs.circle.radius + _rhs.circle.radius:
        return True
    
    # AABB 검사
    min1: Vector2 = _lhs.owner.position + _lhs.aabb.min
    max1: Vector2 = _lhs.owner.position + _lhs.aabb.max
    min2: Vector2 = _rhs.owner.position + _rhs.aabb.min
    max2: Vector2 = _rhs.owner.position + _rhs.aabb.max

    if (min1.x <= max2.x and max1.x >= min2.x and 
        min1.y <= max2.y and max1.y >= min2.y):
        return True

    return False

# TODO: 트리거 판정도 만들기
def IsTrigger(_lhs: CollisionBody, _rhs: CollisionBody) -> bool:
    pass