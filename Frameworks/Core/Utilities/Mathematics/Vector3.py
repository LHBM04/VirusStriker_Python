from typing import final

@final
class Vector3:
    def __init__(self,
                 _x: float = 0.0,
                 _y: float = 0.0,
                 _z: float = 0.0):
        self.__x: float = _x
        self.__y: float = _y
        self.__z: float = _z

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

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, _z: float) -> None:
        self.__z = _z

    # 방향 벡터 (클래스 메서드로 제공)
    @staticmethod
    def Zero() -> 'Vector3':
        return Vector3(0.0, 0.0, 0.0)

    @staticmethod
    def Up() -> 'Vector3':
        return Vector3(0.0, 1.0, 0.0)

    @staticmethod
    def Down() -> 'Vector3':
        return Vector3(0.0, -1.0, 0.0)

    @staticmethod
    def Left() -> 'Vector3':
        return Vector3(-1.0, 0.0, 0.0)

    @staticmethod
    def Right() -> 'Vector3':
        return Vector3(1.0, 0.0, 0.0)

    @staticmethod
    def Forward() -> 'Vector3':
        return Vector3(0.0, 0.0, 1.0)

    @staticmethod
    def Backward() -> 'Vector3':
        return Vector3(0.0, 0.0, -1.0)

    # 연산자 오버로딩
    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + _other.x, self.y + _other.y, self.z + _other.z)

    def __sub__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - _other.x, self.y - _other.y, self.z - _other.z)

    def __mul__(self, _other: float) -> 'Vector3':
        return Vector3(self.x * _other, self.y * _other, self.z * _other)

    def __truediv__(self, _other: float) -> 'Vector3':
        return Vector3(self.x / _other, self.y / _other, self.z / _other)

    def __eq__(self, _other: 'Vector3') -> bool:
        return self.x is _other.x and self.y is _other.y and self.z is _other.z

    def __ne__(self, _other: 'Vector3') -> bool:
        return not self.__eq__(_other)
