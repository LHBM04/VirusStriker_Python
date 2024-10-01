from typing import final
from Utilities.MathF import *

@final
class Vector2:
    def __init__(self, _x: float = 0.0, _y: float = 0.0) -> None:
        self.x: float = _x
        self.y: float = _y

    # 방향벡터
    ZERO: Vector2 = Vector2(0.0, 0.0)
    UP: Vector2 = Vector2(0.0, 1.0)
    DOWN: Vector2 = Vector2(0.0, -1.0)
    LEFT: Vector2 = Vector2(-1.0, 0.0)
    RIGHT: Vector2 = Vector2(1.0, 0.0)

    # 연산자 오버로딩
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __add__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + _other.x, self.y + _other.y)

    def __sub__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - _other.x, self.y - _other.y)

    def __mul__(self, _other: float) -> 'Vector2':
        return Vector2(self.x * _other, self.y * _other)

    def __truediv__(self, _other: float) -> 'Vector2':
        return Vector2(self.x / _other, self.y / _other)

    def __eq__(self, _other: 'Vector2') -> bool:
        return MathF.Equalf(self.x, _other.x) and MathF.Equalf(self.y, _other.y)

    def __ne__(self, _other: 'Vector2') -> bool:
        return not self.__eq__(_other)

    @property
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    @property
    def normalized(self) -> 'Vector2':
        mag = self.magnitude
        if mag == 0:
            return Vector2.Zero()  # 크기가 0인 경우 Zero 벡터 반환
        return Vector2(self.x / mag, self.y / mag)

    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
