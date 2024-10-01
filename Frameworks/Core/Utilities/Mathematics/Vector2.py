class Vector2:
    def __init__(self, _x: float = 0.0, _y: float = 0.0) -> None:
        self.x: float = _x
        self.y: float = _y
    
    # 방향 벡터 (클래스 메서드로 변경)
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
        return MathF.Equalf(float(self.x), _other.x) and MathF.Equalf(float(self.y), _other.y)

    def __ne__(self, _other: 'Vector2') -> bool:
        return not self.__eq__(_other)
