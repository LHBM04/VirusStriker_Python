from typing import final

from .MathF import MathF

@final
class Vector2:
    def __init__(self, _x: float = 0.0, _y: float = 0.0) -> None:
        self.__x: float = _x
        self.__y: float = _y

    # [Operation Override] #
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.__x, -self.__y)

    def __add__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.__x + _other.__x, self.__y + _other.__y)

    def __sub__(self, _other: 'Vector2') -> 'Vector2':
        return Vector2(self.__x - _other.__x, self.__y - _other.__y)

    def __mul__(self, _other: float) -> 'Vector2':
        return Vector2(self.__x * _other, self.__y * _other)

    def __truediv__(self, _other: float) -> 'Vector2':
        return Vector2(self.__x / _other, self.__y / _other)

    def __eq__(self, _other: 'Vector2') -> bool:
        return MathF.Equalf(float(self.__x), _other.__x) and MathF.Equalf(float(self.__y), _other.__y)

    def __ne__(self, _other: 'Vector2') -> bool:
        return not self.__eq__(_other)

    # [Properties] #
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, _x: float) -> None:
        self.__x = _x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, _y: float) -> None:
        self.__y = _y

    @staticmethod
    def Zero() -> 'Vector2':
        return Vector2(0.0, 0.0)

    @staticmethod
    def Up() -> 'Vector2':
        return Vector2(0.0, 1.0)

    @staticmethod
    def Down() -> 'Vector2':
        return Vector2(0.0, -1.0)

    @staticmethod
    def Left() -> 'Vector2':
        return Vector2(-1.0, 0.0)

    @staticmethod
    def Right() -> 'Vector2':
        return Vector2(1.0, 0.0)
