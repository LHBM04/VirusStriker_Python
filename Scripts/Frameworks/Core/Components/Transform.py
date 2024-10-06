from typing import List, Union

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics.Vector2 import Vector2
from Core.Utilities.Mathematics.Vector3 import Vector3

# 객체의 Position, Scale, Rotation 등을 담고 있습니다.
class Transform(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)

        self.__position: Vector3    = Vector3()     # 현재 위치.
        self.__scale: Vector3       = Vector3()     # 현재 크기.
        self.__rotation: Vector3    = Vector3()     # 현재 회전.

        self.__parent: 'Transform'          = None  # 부모 트랜스폼.
        self.__children: List['Transform']  = []    # 모든 자식 트랜스폼.

    # [Properties] #
    def gameObject(self) -> GameObject:
        return None
    
    @property
    def transform(self) -> 'Transform':
        return self

    # 해당 Transform의 Position을 가져옵니다.
    @property
    def position(self) -> Vector3:
        return self.__position

    # 해당 Transform의 Position을 설정합니다.
    @position.setter
    def position(self, _position: Union[Vector2, Vector3]) -> None:
        if isinstance(_position, Vector2):
            self.__position = Vector2(_position.x, _position.y)
        elif isinstance(_position, Vector3):
            self.__position = _position
        else:
            raise ValueError(f"[Oops!] 매개변수가 Vector2, Vector3가 아닙니다!" +
                             f"매개변수는 {type(_position)}이었습니다.")

    # 해당 Transform의 Scale을 가져옵니다.
    @property
    def scale(self) -> Vector3:
        return self.__scale

    # 해당 Transform의 Scale을 설정합니다.
    @scale.setter
    def scale(self, _scale: Union[Vector2, Vector3]) -> None:
        if isinstance(_scale, Vector2):
            self.__position = Vector2(_scale.x, _scale.y)
        elif isinstance(_scale, Vector3):
            self.__position = _scale
        else:
            raise ValueError(f"[Oops!] 매개변수가 Vector2, Vector3가 아닙니다!" +
                             f"매개변수는 {type(_scale)}이었습니다.")

    # 해당 Transform의 Rotation을 가져옵니다.
    @property
    def rotation(self) -> Vector3:
        return self.__rotation

    # 해당 Transform의 Rotation을 설정합니다.
    @rotation.setter
    def rotation(self, _rotation: Union[Vector2, Vector3]) -> None:
        if isinstance(_rotation, Vector2):
            self.__position = Vector2(_rotation.x, _rotation.y)
        elif isinstance(_rotation, Vector3):
            self.__position = _rotation
        else:
            raise ValueError(f"[Oops!] 매개변수가 Vector2, Vector3가 아닙니다!" +
                             f"매개변수는 {type(_rotation)}이었습니다.")

    # 해당 Transform의 부모 Transform을 가져옵니다. (Read-Only)
    @property
    def parent(self) -> 'Transform':
        return self.__parent

    # 해당 Transform의 자식 Transform을 가져옵니다. (Read-Only)
    @property
    def children(self) -> List['Transform']:
        return self.__children

    # [Methods]
    # 해당 인덱스에 있는 자식 Transform을 가져옵니다.
    def GetChild(self, _index: Union[int, str]) -> 'Transform':
        if isinstance(_index, int):
            if (_index < 0 or
                _index >= len(self.__children)):
                raise ValueError(f"[Oops!] 인덱스가 해당 범위를 벗어났습니다.")

            return self.__children[_index]
        elif isinstance(_index, str):
            if (_index is None or
                _index == ""):
                raise ValueError(f"[Oops!] 인덱스가 해당 범위를 벗어났습니다.")

            for currentChild in self.__children:
                if currentChild.name is _index:
                    return currentChild

            return None
        else:
            raise ValueError(f"[Oops!] 인덱스가 틀렸거나, 해당 인덱스에 자식 Transform이 존재하지 않습니다. " +
                             f"검색한 인덱스는 {str(_index)}였습니다.")