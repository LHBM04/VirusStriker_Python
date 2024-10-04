from logging import fatal
from typing import final
from typing import List
from dataclasses import dataclass

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics import Vector2

# 로테이션 정보
@dataclass
class Rotation:
    __x: bool     # x축 뒤집기 여부
    __y: bool     # y축 뒤집기 여부
    __z: float    # z축 회전값 

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

# 오브젝트의 위치, 크기, 회전값 등을 저장하는 컴포넌트
@final
class Transform(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)

        self.__position: Vector2              = Vector2(0.0, 0.0)  # 현재 포지션
        self.__scale: Vector2                 = Vector2(0.0, 0.0)       # 현재 크기
        self.__rotation: Rotation             = Rotation(False, False, 0.0)    # 현재 회전값. (X, Y축은 Boolean.)

        self.__parent: 'Transform'            = None                      # 부모 트랜스폼
        self.__children: List['Transform']    = []                        # 자식 트랜스폼

    @property
    def position(self) -> Vector2:
        return self.__position

    @position.setter
    def position(self, _newPosition: Vector2) -> None:
        self.__position = _newPosition

    @property
    def scale(self) -> Vector2:
        return self.__scale

    @scale.setter
    def scale(self, _newScale: Vector2) -> None:
        self.__scale = _newScale

    @property
    def rotation(self) -> Rotation:
        return self.__rotation