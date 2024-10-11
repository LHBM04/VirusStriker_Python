from __future__ import annotations  # Future annotations
from typing import List, Union

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject
from Core.Utilities.Mathematics import Vector2, Vector3

class Transform(Component):
    def __init__(self, _owner: GameObject):  # GameObject를 문자열로 사용
        super().__init__(_owner)

        self.__position: Vector2            = Vector2()  # 포지션
        self.__scale: Vector2               = Vector2()      # 크기
        self.__rotation: float              = 0              # 회전 각도(Z축)

        self.__parent: Transform | None     = None  # 부모 Transform
        self.__children: List[Transform]    = []   # 자식 Transform

 # region [Properties]
    @property
    def position(self) -> Vector2:
        return self.__position

    @position.setter
    def position(self, _position: Union[Vector2, Vector3]) -> None:
        if isinstance(_position, (Vector2, Vector3)):
            self.__position = Vector2(_position.x, _position.y)
            if self.__children:
                for child in self.__children:
                    child.position = child.localPosition + self.__position
                    child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                    child.rotation = child.localRotation + self.__rotation
        else:
            raise ValueError(f"[Oops!] 매개변수가 Vector2, Vector3가 아닙니다! 매개변수는 {type(_position)}이었습니다.")

    @property
    def localPosition(self) -> Vector2:
        if self.__parent is not None:
            return self.__position - self.__parent.position
        return self.__position

    @localPosition.setter
    def localPosition(self, _localPosition: Vector2) -> None:
        if self.__parent is not None:
            self.__position = _localPosition + self.__parent.position
        else:
            self.__position = _localPosition
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def scale(self) -> Vector2:
        return self.__scale

    @scale.setter
    def scale(self, _scale: Union[Vector2, Vector3]) -> None:
        if isinstance(_scale, (Vector2, Vector3)):
            self.__scale = Vector2(_scale.x, _scale.y)
            if self.__children:
                for child in self.__children:
                    child.position = child.localPosition + self.__position
                    child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                    child.rotation = child.localRotation + self.__rotation
        else:
            raise ValueError(f"[Oops!] 매개변수가 Vector2, Vector3가 아닙니다! 매개변수는 {type(_scale)}이었습니다.")

    @property
    def localScale(self) -> Vector2:
        if self.__parent is not None:
            return Vector2(self.__scale.x / self.__parent.scale.x, self.__scale.y / self.__parent.scale.y)
        return self.__scale

    @localScale.setter
    def localScale(self, _localScale: Vector2) -> None:
        if self.__parent is not None:
            self.__scale = Vector2(_localScale.x * self.__parent.scale.x, _localScale.y * self.__parent.scale.y)
        else:
            self.__scale = _localScale
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def rotation(self) -> float:
        return self.__rotation

    @rotation.setter
    def rotation(self, _rotation: float) -> None:
        if isinstance(_rotation, (float, int)):
            self.__rotation = _rotation
            if self.__children:
                for child in self.__children:
                    child.position = child.localPosition + self.__position
                    child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                    child.rotation = child.localRotation + self.__rotation
        else:
            raise ValueError(f"[Oops!] 회전 값은 float 또는 int여야 합니다! 매개변수는 {type(_rotation)}이었습니다.")

    @property
    def localRotation(self) -> float:
        if self.__parent is not None:
            return self.__rotation - self.__parent.rotation
        return self.__rotation

    @localRotation.setter
    def localRotation(self, _localRotation: float) -> None:
        if self.__parent is not None:
            self.__rotation = _localRotation + self.__parent.rotation
        else:
            self.__rotation = _localRotation
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def parent(self) -> Transform:
        return self.__parent

    @parent.setter
    def parent(self, _parent: Transform) -> None:
        self.__parent = _parent
        _parent.__children.append(self)
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def children(self) -> List[Transform]:
        return self.__children
    # endregion
    # region Life-Cycle
    def Start(self) -> None:
        super().Start()

    def OnDestroy(self) -> None:
        super().OnDestroy()
    # endregion