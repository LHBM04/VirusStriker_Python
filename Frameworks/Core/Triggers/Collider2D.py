from abc import ABC, abstractmethod
from enum import Enum


# 충돌 검사를 위한 열거형.
# 필요한 게 있을 때마다 추가하여 쓰도록 하자
class EColliderTag(Enum):
    NONE    = 0  # 더미 태그(기본).
    HARMFUL = 1  # 플레이어에게 해로운 오브젝트의 태그
    LETHAL  = 2  # 플레이어에게 치명적인(즉사) 오브젝트의 태그

# Collider2D 베이스
class Collider2D(ABC):
    def __init__(self, _owner: 'Actor') -> None:
        from Frameworks.Core.Objects.Actors.Actor import Actor

        self.owner: Actor = _owner
        self.tag: EColliderTag = EColliderTag.NONE
        self.useTrigger = False

    @abstractmethod
    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass
    
    @abstractmethod
    def IsTrigger(self, _other: 'Collider2D') -> bool:
        pass
