from typing import final

@final
class Color:
    @staticmethod
    def minValue() -> int:
        return 0
    
    @staticmethod
    def maxValue() -> int:
        return 255
    
    def __init__(self, 
                 _r: int = maxValue(), 
                 _g: int = maxValue(), 
                 _b: int = maxValue(), 
                 _a: int = maxValue()) -> None:
        self.r = max(self.minValue(), min(_r, self.maxValue()))
        self.g = max(self.minValue(), min(_g, self.maxValue()))
        self.b = max(self.minValue(), min(_b, self.maxValue()))
        self.a = max(self.minValue(), min(_a, self.maxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return self.r == _other.r and self.g == _other.g and self.b == _other.b and self.a == _other.a

    def __ne__(self, _other: 'Color') -> bool:
        return not self.__eq__(_other)