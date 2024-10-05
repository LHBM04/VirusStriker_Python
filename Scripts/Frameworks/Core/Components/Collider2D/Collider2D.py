from abc import ABCMeta, abstractmethod
from enum import Enum

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics.Vector2 import Vector2

# 충돌 검사를 위한 열거형.
# 필요한 게 있을 때마다 추가하여 쓰도록 하자
class EColliderTag(Enum):
    NONE    = 0  # 더미 태그(기본).
    HARMFUL = 1  # 플레이어에게 해로운 오브젝트의 태그
    LETHAL  = 2  # 플레이어에게 치명적인(즉사) 오브젝트의 태그

# Collider2D 베이스
class Collider2D(metaclass = ABCMeta, Component):
    def __init__(self, _owner: GameObject) -> None:
        super().__init__(_owner)

        self.__tag: EColliderTag    = EColliderTag.NONE
        self.__useTrigger           = False

    @property
    def tag(self) -> EColliderTag:
        return self.__tag

    @tag.setter
    def tag(self, _newTag: EColliderTag) -> None:
        self.__tag = _newTag

    @property
    def useTrigger(self) -> bool:
        return self.__useTrigger

    @useTrigger.setter
    def useTrigger(self, _useTrigger: bool):
        self.__useTrigger = _useTrigger

    @abstractmethod
    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass
    
    @abstractmethod
    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass



