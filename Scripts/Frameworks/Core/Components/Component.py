from abc import ABCMeta
from typing import final, Iterator, List, Dict, Type, TypeVar, Sequence

from Core.Components.Object import Object

class Component(Object, metaclass = ABCMeta):
    def __init__(self, _owner: 'GameObject'):
        from Core.Components.GameObject import GameObject

        super().__init__()

        self.__owner: GameObject        = _owner

        self.Awake()

    #region [Properties]
    @property
    def name(self) -> str:
        return self.__owner.name

    @name.setter
    def name(self, _name) -> None:
        self.__owner.name = _name

    @property
    def gameObject(self) -> 'GameObject':
        return self.__owner

    @property
    def transform(self) -> 'Transform':
        return self.__owner.transform

    def Awake(self):
        pass

    def Start(self):
        pass

    def OnDestroy(self):
        pass

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

@final
class ComponentManager:
    def __init__(self, _owner: 'GameObject'):
        self.__owner                                                = _owner
        self.__components: Dict[Type[TComponent], TComponent]       = {}
        self.__addComponents: Dict[Type[TComponent], TComponent]    = {}

    #region [Properties]
    @property
    def gameObject(self) -> 'GameObject':
        return self.__owner

    @property
    def transform(self) -> 'Transform':
        return self.__owner.transform
    #endregion
    #region [Operators Override]
    def __iter__(self) -> Iterator[TComponent]:
        return iter(self.__components)

    def __getitem__(self, _index: Type[TComponent]) -> TComponent:
        return self.GetComponent(_index)

    def __len__(self) -> int:
        return len(self.__components)
    #endregion
    #region [Methods]
    # 관리 중인 Component를 가져옵니다.
    def GetComponent(self, _componentType: Type[TComponent]) -> TComponent:
        return self.__components[_componentType] if _componentType in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_componentsType: Type[TComponent]) -> Sequence[TComponent]:
        return [self.__components[component] for component in _componentsType if component in self.__components]

    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        newComponent: TComponent = _component(self.__owner)
        self.__addComponents[_component] = newComponent
        return newComponent

    def AddComponents(self, *_components: Type[TComponent]) -> Sequence[TComponent]:
        newComponents: List[TComponent] = []
        for currentComponent in _components:
            if currentComponent in self.__components:
                raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {currentComponent}")
            else:
                newComponent: TComponent = currentComponent(self.__owner)
                self.__addComponents[currentComponent] = newComponent
                newComponents.append(newComponent)

        return newComponents

    def RemoveComponent(self, _component: Type[TComponent]) -> bool:
        return True

    def RemoveComponents(self, *_components: Type[TComponent]) -> bool:
        return True

    def RemoveAllComponents(self) -> bool:
        return True
    # endregion
    def Update(self, _deltaTime: float):
        if self.__addComponents:
            for newComponent in self.__addComponents.values():
                self.__components[type(newComponent)] = newComponent  # __components에 추가
                newComponent.Start()  # Start 메서드 호출
            self.__addComponents.clear()

    def FixedUpdate(self, _fixedDeltaTime: float):
        if len(self.__components) > 0:
            for component in self.__components.values():
                if component.isDestroy:
                    key: Type[TComponent] = next(key for key, value in self.__components.items() if value is component)
                    self.__components.pop(key).OnDestroy()
