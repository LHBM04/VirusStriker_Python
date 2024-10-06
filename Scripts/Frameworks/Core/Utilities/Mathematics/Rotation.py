from dataclasses import dataclass
from logging import fatal


# 로테이션 정보
@dataclass
class Rotation:
    def __init__(self, _x: bool = False, _y: bool = False, _z: float = 0.0):
        __x: bool = _x  # x축 뒤집기 여부
        __y: bool = _y  # y축 뒤집기 여부
        __z: float = _z # z축 회전값

    @property
    def x(self) -> bool:
        return self.__x

    @x.setter
    def x(self, _isFlip: bool) -> None:
        self.__x = _isFlip

    @property
    def y(self) -> bool:
        return self.__y

    @y.setter
    def y(self, _isFlip: bool) -> None:
        self.__y = _isFlip

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, _z: float) -> None:
        self.__z = _z