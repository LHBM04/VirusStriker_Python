import numpy as np
from typing import final

@final
class Vector3:
    def __init__(self, _x: float, _y: float, _z: float) -> None:
        self.x = _x
        self.y = _y
        self.z = _z
    
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

    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x + _other.x, self.y + _other.y, self.z + _other.z)

    def __sub__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x - _other.x, self.y - _other.y, self.z - _other.z)

    def __mul__(self, _other: 'Vector3') -> 'Vector3':
        return Vector3(self.x * _other.x, self.y * _other.y, self.z * _other.z)
    
    def __mul__(self, _other: float) -> 'Vector3':
        return Vector3(self.x * _other, self.y * _other, self.z * _other)
    
    def __truediv__(self, other: 'Vector3') -> 'Vector3':
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
    
    def __truediv__(self, other: float) -> 'Vector3':
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __eq__(self, _other: 'Vector3') -> bool:
        return self.x == _other.x and self.y == _other.y and self.z == _other.z

    def __ne__(self, _other: 'Vector3') -> bool:
        return not self.__eq__(_other)

    def __str__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

    @property
    def magnitude(self) -> float:
        """Returns the magnitude (length) of the vector."""
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def unit(self) -> 'Vector3':
        """Returns the unit vector (normalized vector)."""
        mag = self.magnitude
        if mag == 0:
            return Vector3(0, 0, 0)  # Return zero vector if magnitude is zero
        return Vector3(self.x / mag, self.y / mag, self.z / mag)
