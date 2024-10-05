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
        self.__r: int = max(self.MinValue(), min(_r, self.MaxValue()))
        self.__g: int = max(self.MinValue(), min(_g, self.MaxValue()))
        self.__b: int = max(self.MinValue(), min(_b, self.MaxValue()))
        self.__a: int = max(self.MinValue(), min(_a, self.MaxValue()))

    @property
    def r(self) -> int:
        return self.__r

    @r.setter
    def r(self, _r: int) -> None:
        self.__r = max(self.MinValue(), min(_r, self.MaxValue()))

    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, _g: int) -> None:
        self.__g = max(self.MinValue(), min(_g, self.MaxValue()))

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, _b: int) -> None:
        self.__r = max(self.MinValue(), min(_b, self.MaxValue()))

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, _a: int) -> None:
        self.__a = max(self.MinValue(), min(_a, self.MaxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return (self.r == _other.r and
                self.g == _other.g and
                self.b == _other.b and
                self.a == _other.a)

    def __ne__(self, _other: 'Color') -> bool:
        return not self.__eq__(_other)

COLOR_RED: Color        = Color(255, 0, 0)
COLOR_GREEN: Color      = Color(0, 255, 0)
COLOR_BLUE: Color       = Color(0, 0, 255)
COLOR_YELLOW: Color     = Color(255, 255, 0)
COLOR_CYAN: Color       = Color(0, 255, 255)
COLOR_MAGENTA: Color    = Color(255, 0, 255)
COLOR_WHITE: Color      = Color(255, 255, 255)
COLOR_BLACK: Color      = Color(0, 0, 0)
COLOR_GRAY: Color       = Color(128, 128, 128)
COLOR_ORANGE: Color     = Color(255, 165, 0)
