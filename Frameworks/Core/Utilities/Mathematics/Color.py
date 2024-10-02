from typing import final

@final
class Color:
    @staticmethod
    def MinValue() -> int:
        return 0
    
    @staticmethod
    def MaxValue() -> int:
        return 255
    
    def __init__(self,
                 _r: int = MaxValue(),
                 _g: int = MaxValue(),
                 _b: int = MaxValue(),
                 _a: int = MaxValue()) -> None:
        self.r: int = max(self.MinValue(), min(_r, self.MaxValue()))
        self.g: int = max(self.MinValue(), min(_g, self.MaxValue()))
        self.b: int = max(self.MinValue(), min(_b, self.MaxValue()))
        self.a: int = max(self.MinValue(), min(_a, self.MaxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return self.r == _other.r and self.g == _other.g and self.b == _other.b and self.a == _other.a

    def __ne__(self, _other: 'Color') -> bool:
        return not self.__eq__(_other)