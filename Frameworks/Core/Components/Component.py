from abc import ABC, abstractmethod
from logging import fatal
from typing import final, Set, Dict
from typing import Type, TypeVar

# 모든 컴포넌트의 베이스 클래스
class Component(ABC):
    def __init__(self, _owner: 'GameObject'):
        from Frameworks.Core.Components.GameObject import GameObject
        self.owner: GameObject = _owner # 해당 컴포넌트를 소지하고 있는 게임 오브젝트.

    @abstractmethod
    def OnAdd(self):
        pass

    @abstractmethod
    def OnUpdate(self):
        pass

    @abstractmethod
    def OnDelete(self):
        pass

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

# 오브젝트의 모든 컴포넌트를 관리합니다.
@final
class ComponentManager:
    def __init__(self):
        self.components: Dict[Type[TComponent] : Component] = { }

    # 컴포넌트를 추가합니다.
    def AddComponent(self, component: Component) -> bool:
        if type(component) in self.components.keys():
            return False

        self.components[type(component)] = component
        return True

    # 컴포넌트들을 추가합니다.
    def AddComponents(self, _components: Set[Component]) -> bool:
        for currentComponent in self.components:
            if type(currentComponent) in self.components.keys():
                return False

        for currentComponent in self.components:
            self.components[type(currentComponent)] = currentComponent

        return True

    # 소지하고 있는 컴포넌트를 가져옵니다.
    def GetComponent(self, _componentType: Type[TComponent]) -> Component:
        if _componentType not in self.components.keys():
            raise ValueError(f"[Oops!] 포함되지 않은 컴포넌트입니다. 검색하려던 컴포넌트는 \"{str(_componentType)}\"였습니다.")

        return self.components[_componentType]

    def RemoveComponent(self, _componentType: Type[TComponent]) -> bool:
        if _componentType not in self.components.keys():
            raise ValueError(f"[Oops!] 포함되지 않은 컴포넌트입니다. 검색하려던 컴포넌트는 \"{str(_componentType)}\"였습니다.")

        self.components.pop(_componentType)
        return True