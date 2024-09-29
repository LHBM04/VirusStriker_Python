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
