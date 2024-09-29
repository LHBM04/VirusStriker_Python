from typing import final

from Utilities.MathF import *

@final
class Vector2:
    def __init__(self, _x: float = 0, _y: float = 0) -> None:
        self.m_x: float = _x
        self.m_y: float = _y

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.m_x, -self.m_y)

    def __add__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.m_x + _other.m_x, self.m_y + _other.m_y)

    def __sub__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.m_x - _other.m_x, self.m_y - _other.m_y)

    def __mul__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.m_x * _other, self.m_y * _other)
    
    def __truediv__(self, other):
        return Vector2(self.m_x / other, self.m_y / other)
