from abc import ABCMeta, abstractmethod
from typing import final, Set, Dict
from typing import Type, TypeVar

from Core.Components.GameObject import GameObject

# 모든 컴포넌트의 베이스 클래스
class Component(metaclass = ABCMeta):
    def __init__(self, _owner: GameObject):
        self.owner: GameObject = _owner # 해당 컴포넌트를 소지하고 있는 게임 오브젝트.

    # 해당 컴포넌트가 추가되었을 때 호출됩니다.
    @abstractmethod
    def OnAdd(self):
        pass

    # 해당 컴포넌트를 소지한 오브젝트의 Update()에서 같이 실행됩니다.
    @abstractmethod
    def OnUpdate(self, _deltaTime: float):
        pass

    # 해당 컴포넌트를 소지한 오브젝트의 FixedUpdate()에서 같이 실행됩니다.
    @abstractmethod
    def OnFixedUpdate(self, _fixedDeltaTime: float):
        pass

    # 해당 컴포넌트가 삭제되었을 떄 호출됩니다.
    @abstractmethod
    def OnDelete(self):
        pass

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

# 오브젝트의 모든 컴포넌트를 관리합니다.
@final
class ComponentManager:
    def __init__(self):
        self.__components: Dict[Type[TComponent]: Component] = { }

    # 컴포넌트를 추가합니다.
    def AddComponent(self, component: Component) -> bool:
        if type(component) in self.__components.keys():
            return False

        self.__components[type(component)] = component
        component.OnAdd()
        return True

    # 컴포넌트들을 추가합니다.
    def AddComponents(self, _components: Set[Component]) -> bool:
        for currentComponent in self.__components:
            if type(currentComponent) in self.__components.keys():
                return False
            else:
                self.__components[type(currentComponent)] = currentComponent
                currentComponent.OnAdd()

        return True

    # 소지하고 있는 컴포넌트를 가져옵니다.
    def GetComponent(self, _componentType: Type[TComponent]) -> Component:
        if _componentType not in self.__components.keys():
            raise ValueError(f"[Oops!] 포함되지 않은 컴포넌트입니다. 검색하려던 컴포넌트는 \"{str(_componentType)}\"였습니다.")

        return self.__components[_componentType]

    # 소지하고 있는 컴포넌트를 삭제합니다.
    def RemoveComponent(self, _componentType: Type[TComponent]) -> bool:
        if _componentType not in self.__components.keys():
            raise ValueError(f"[Oops!] 포함되지 않은 컴포넌트입니다. 검색하려던 컴포넌트는 \"{str(_componentType)}\"였습니다.")

        delObject: Component = self.__components.pop(_componentType)
        delObject.OnDelete()
        return True

    # 소지하고 있는 컴포넌트의 Update()를 합니다.
    def Update(self, _deltaTime: float) -> None:
        for currentComponent in self.__components.values():
            currentComponent.OnUpdate(_deltaTime)

    # 소지하고 잇는 컴포넌트의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        for currentComponent in self.__components.values():
            currentComponent.OnUpdate(_fixedDeltaTime)