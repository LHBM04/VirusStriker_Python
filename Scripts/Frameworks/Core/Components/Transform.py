from typing import final
from typing import List


from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics.Rotation import Rotation
from Core.Utilities.Mathematics.Vector2 import Vector2

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

    def OnUpdate(self, _deltaTime: float):
        pass