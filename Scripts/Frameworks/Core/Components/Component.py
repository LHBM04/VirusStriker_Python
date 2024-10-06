from abc import ABCMeta, abstractmethod

from Core.Components.Object import Object
from Core.Components.GameObject import GameObject
from Core.Components.Transform import Transform

class Component(Object, metaclass = ABCMeta):
    def __init__(self, _owner: GameObject):
        super().__init__()
        self.__owner: GameObject = _owner

    # [Property Methods]
    # 해당 컴포넌트가 붙어있는 오브젝트(오너)를 반환합니다. (Read-Only)
    @property
    @abstractmethod
    def gameObject(self) -> GameObject:
        return self.__owner

    # 해당 컴포넌트가 붙어있는 오브젝트(오너)의 트랜스폼을 반환합니다. (Read-Only)
    @property
    @abstractmethod
    def transform(self) -> Transform:
        return self.__owner.transform