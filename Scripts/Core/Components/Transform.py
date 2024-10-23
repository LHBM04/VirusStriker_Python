from __future__ import annotations
from typing import List, Union, Optional

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject
from Core.Utilities.Mathematics import Vector2

class Transform(Component):
    def __init__(self, _owner: GameObject):  # GameObject를 문자열로 사용
        super().__init__(_owner)

        self.__position: Vector2            = Vector2(0, 0)     # 포지션
        self.__scale: Vector2               = Vector2(0, 0)     # 크기
        self.__rotation: float              = 0             # 회전 각도(Z축)

        self.__parent: Optional[Transform]  = None          # 부모 Transform
        self.__children: List[Transform]    = []            # 자식 Transform

    # region Properties
    @property
    def position(self) -> Vector2:
        """
        Transform의 현재 월드 위치를 반환합니다.
        :return: 현재 Vector2로 된 월드 위치.
        """
        return self.__position

    @position.setter
    def position(self, _position: Vector2) -> None:
        """
        Transform의 월드 위치를 설정합니다.
        :param _position: Vector2 또는 Vector3 객체로 된 위치 값.
        """
        self.__position = Vector2(_position.x, _position.y)
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation


    @property
    def localPosition(self) -> Vector2:
        """
        Transform의 로컬 좌표를 반환합니다.
        :return: 현재 Vector2로 된 로컬 좌표.
        """
        if self.__parent is not None:
            return self.__position - self.__parent.position

        return self.__position

    @localPosition.setter
    def localPosition(self, _localPosition: Vector2) -> None:
        """
        Transform의 로컬 좌표를 설정합니다.
        :param _localPosition: Vector2 객체로 된 로컬 좌표 값.
        """
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
        """
        Transform의 크기를 반환합니다.
        :return: 현재 Vector2로 된 크기.
        """
        return self.__scale

    @scale.setter
    def scale(self, _scale: Vector2) -> None:
        """
        Transform의 크기를 설정합니다.
        :param _scale: Vector2 또는 Vector3 객체로 된 크기 값.
        """
        self.__scale = Vector2(_scale.x, _scale.y)
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def localScale(self) -> Vector2:
        """
        Transform의 로컬 크기를 반환합니다.
        :return: 현재 Vector2로 된 로컬 크기.
        """
        if self.__parent is not None:
            return Vector2(self.__scale.x / self.__parent.scale.x, self.__scale.y / self.__parent.scale.y)
        return self.__scale

    @localScale.setter
    def localScale(self, _value: Vector2) -> None:
        """
        Transform의 로컬 크기를 설정합니다.
        :param _value: Vector2 객체로 된 로컬 크기 값.
        """
        if self.__parent is not None:
            self.__scale = Vector2(_value.x * self.__parent.scale.x, _value.y * self.__parent.scale.y)
        else:
            self.__scale = _value
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def rotation(self) -> float:
        """
        Transform의 회전 각도를 반환합니다.
        :return: 현재 Z축을 기준으로 한 회전 각도.
        """
        return self.__rotation

    @rotation.setter
    def rotation(self, _rotation: float) -> None:
        """
        Transform의 회전 각도를 설정합니다.
        :param _rotation: float 또는 int로 된 회전 각도 값.
        """
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
        """
        Transform의 로컬 회전 각도를 반환합니다.
        :return: 현재 Z축을 기준으로 한 로컬 회전 각도.
        """
        if self.__parent is not None:
            return self.__rotation - self.__parent.rotation
        return self.__rotation

    @localRotation.setter
    def localRotation(self, _localRotation: float) -> None:
        """
        Transform의 로컬 회전 각도를 설정합니다.
        :param _localRotation: float로 된 로컬 회전 각도 값.
        """
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
        """
        부모 Transform을 반환합니다.
        :return: 현재 부모 Transform.
        """
        return self.__parent

    @parent.setter
    def parent(self, _parent: Transform) -> None:
        """
        부모 Transform을 설정합니다.
        :param _parent: 부모가 될 Transform 객체.
        """
        self.__parent = _parent
        _parent.__children.append(self)
        if self.__children:
            for child in self.__children:
                child.position = child.localPosition + self.__position
                child.scale = Vector2(child.localScale.x * self.__scale.x, child.localScale.y * self.__scale.y)
                child.rotation = child.localRotation + self.__rotation

    @property
    def children(self) -> List[Transform]:
        """
        자식 Transform 목록을 반환합니다.
        :return: 현재 모든 자식 Transform의 리스트.
        """
        return self.__children
    # endregion
    # region Life-Cycle
    def Start(self) -> None:
        super().Start()

    def OnDestroy(self) -> None:
        super().OnDestroy()
    # endregion