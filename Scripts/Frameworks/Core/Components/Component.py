from abc import ABCMeta, abstractmethod
from typing import final, Iterator, List, Dict, Type, TypeVar

from Core.Components.Object import Object


class Component(Object, metaclass = ABCMeta):
    def __init__(self, _owner: 'GameObject'):
        from Core.Components.GameObject import GameObject

        super().__init__()
        self.__owner: GameObject = _owner

    #region [Property Methods]
    @property
    def name(self) -> str:
        return self.gameObject.name

    @name.setter
    def name(self, _name: str) -> None:
        self.gameObject.name = _name

    from Core.Components.GameObject import GameObject
    # 해당 컴포넌트가 붙어있는 오브젝트(오너)를 반환합니다. (Read-Only)
    @property
    def gameObject(self) -> 'GameObject':
        return self.__owner

    from Core.Components.GameObject import Transform
    # 해당 컴포넌트가 붙어있는 오브젝트(오너)의 트랜스폼을 반환합니다. (Read-Only)
    @property
    def transform(self) -> 'Transform':
        return self.__owner.transform
    #endregion

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

@final
class ComponentManager:
    def __init__(self, _owner: 'GameObject'):
        from Core.Components.GameObject import GameObject

        self.__owner: GameObject                                    = _owner  # 관리 중인 Component들의 주인.
        self.__components: Dict[Type[TComponent], TComponent]       = {}  # 관리 중인 Component.
        self.__addComponents: Dict[Type[TComponent], TComponent]    = {}  # 추가할 Component.

    # [Operators Override] #
    def __iter__(self) -> Iterator[TComponent]:
        return iter(self.__components)

    def __getitem__(self, _index: Type[TComponent]) -> TComponent:
        return self.GetComponent(_index)

    def __len__(self) -> int:
        return len(self.__components)

    # [Methods] #
    # 관리 중인 Component를 가져옵니다.
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__components[_component] if _component in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return [self.__components[component] for component in _components if component in self.__components]

    def AddComponent(self, _component: Type[TComponent]) -> bool:
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        self.__addComponents[type(_component)] = _component(self.__owner)
        return True

    def AddComponents(self, *_components: Type[TComponent]) -> bool:
        for currentComponent in _components:
            if currentComponent in self.__components:
                raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {currentComponent}")
            else:
                self.__addComponents[type(currentComponent)] = currentComponent(self.__owner)

        return True
