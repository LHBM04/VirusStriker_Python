import numpy as np

from Utilities.MathF import *

class Vector2:
    def __init__(self, _x: float = 0, _y: float = 0) -> None:
        self.m_x: float = _x
        self.m_y: float = _y

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __add__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + _other.x, self.y + _other.y)

    def __sub__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - _other.x, self.y - _other.y)

    def __mul__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x * _other, self.y * _other)

    def __truediv__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.x / _other, self.y / _other)

    def __floor__(self) -> 'Vector2':
        return Vector2(MathF.Floor(self.x), MathF.Floor(self.y))

    def __ceil__(self) -> 'Vector2':
        return Vector2(MathF.Ceil(self.x), MathF.Ceil(self.y))

    def magnitude(self) -> float:
        return np.sqrt(self.m_x ** 2 + self.m_y ** 2)
    
    def dot(self, _other: 'Vector2') -> float:
        return np.dot([self.m_x, _other.m_y], [self.m_x, _other.m_y])