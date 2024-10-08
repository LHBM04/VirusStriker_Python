from abc import ABCMeta
from typing import final, Iterator, List, Dict, Type, TypeVar

from Core.Components.Object import Object

class Component(Object, metaclass = ABCMeta):
    def __init__(self, _owner: 'GameObject'):
        super().__init__()

        from Core.Components.GameObject import GameObject
        self.__owner: GameObject = _owner
        self.__isActive: bool = True

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
    #endregion

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

@final
class ComponentManager:
    def __init__(self, _owner: 'GameObject'):
        self.__owner                                            = _owner
        self.__components: Dict[Type[TComponent], TComponent]   = {}

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
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__components[_component] if _component in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return [self.__components[component] for component in _components if component in self.__components]

    def AddComponent(self, _component: Type[TComponent]) -> Component:
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        newComponent: TComponent = _component(self.__owner)
        self.__components[_component] = newComponent
        return newComponent

    def AddComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        newComponents: List[TComponent] = []
        for currentComponent in _components:
            if currentComponent in self.__components:
                raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {currentComponent}")
            else:
                newComponent: TComponent = currentComponent(self.__owner)
                self.__components[currentComponent] = newComponent
                newComponents.append(newComponent)

        return newComponents
    #endregion
