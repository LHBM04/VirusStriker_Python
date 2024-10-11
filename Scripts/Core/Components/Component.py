from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import final, Iterator, List, Dict, Type, TypeVar, Sequence

from Core.Objects.GameObject import GameObject
from Core.Objects.Object import Object

class Component(Object, metaclass = ABCMeta):
    """
    Game Object의 정보 및 속성을 저장하고 제어합니다.
    """
    def __init__(self, _owner: GameObject):
        super().__init__()

        self.__owner: GameObject = _owner # 해당 Component의 주인.

    # region Properties
    @property
    def gameObject(self) -> GameObject:
        """
        해당 Component의 Owner를 반환합니다.
        :return: 해당 Component의 Owner.
        """
        return self.__owner

    @property
    def name(self) -> str:
        """
        해당 Component의 Owner의 이름을 반환합니다.
        :return: 해당 Component의 Owner의 이름.
        """
        return self.__owner.name
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self) -> None:
        """
        해당 Component가 추가되었을 때 한번 실행됩니다.
        (※ 해당 Component를 사용하는 Game Object에 추가된 시점을 의미합니다.)
        """
        super().Start()

    @abstractmethod
    def OnDestroy(self) -> None:
        """
        해당 Component가 파괴될 때 한번 실행됩니다.
        (※ 해당 Component를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        super().OnDestroy()
    # endregion

# 제네릭(Component를 상속받은 클래스만 가능하게끔 제한).
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

@final
class ComponentController:
    """
    Game Object에 추가되어 있는 모든 Component를 제어합니다.
    """
    def __init__(self, _owner: GameObject):
        self.__owner: GameObject                                = _owner # 해당 Controller의 주인(Owner).
        self.__components: Dict[Type[TComponent], TComponent]   = {}     # 관리하고 있는 모든 Component.

    # region Properties
    @property
    def gameObject(self) -> GameObject:
        """
        해당 Component의 Owner를 반환합니다.
        :return: 해당 Component의 Owner.
        """
        return self.__owner
    @property
    def name(self) -> str:
        """
        해당 Component의 Owner의 이름을 반환합니다.
        :return: 해당 Component의 Owner의 이름.
        """
        return self.__owner.name
    # endregion
    # region Operators Override
    def __iter__(self) -> Iterator[TComponent]:
        """
        관리하는 모든 Component를 순회할 수 있도록 Iterator를 반환합니다.
        :return: 관리하는 모든 Component iterator.
        """
        return iter(self.__components)

    def __getitem__(self, _component: Type[TComponent]) -> TComponent:
        """
        주어진 타입의 Component를 반환합니다.
        :param _component: 접근할 Component의 타입.
        :return: 해당 타입의 Component.
        """
        return self.__components[_component]

    def __len__(self) -> int:
        """
        관리하는 Component의 개수를 반환합니다.
        :return: Component의 총 개수.
        """
        return len(self.__components)
    # endregion
    # region Component Methods
    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        """
        새로운 Component를 추가합니다.\n
        (※ 중복되는 Component는 허용하지 않습니다.)
        :param _component: 추가할 Component의 타입.
        :return: 추가한 Component의 인스턴스.
        """
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        self.__components[_component] = _component(self.__owner)
        return self.__components[_component]

    def AddComponents(self, *_components: Type[TComponent]) -> Sequence[TComponent]:
        """
        새로운 Component들을 추가합니다.\n
        (※ 중복되는 Component는 허용하지 않습니다.)
        :param _components: 추가할 Component들의 타입들.
        :return: 추가한 Component들의 인스턴스 List.
        """
        newComponents: List[TComponent] = []
        for currentComponent in _components:
            if currentComponent in self.__components:
                raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {currentComponent}")
            else:
                self.__components[currentComponent] = currentComponent(self.__owner)
                newComponents.append(self.__components[currentComponent])

        return newComponents

    def GetComponent(self, _componentType: Type[TComponent]) -> TComponent:
        """
        관리하고 있는 Component를 반환합니다.
        :param _componentType: 검색할 Component의 타입.
        :return: 해당 타입의 Component를 관리하고 있다면 해당 Component의 인스턴스, 없다면 None.
        """
        return self.__components[_componentType] if _componentType in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_componentsType: Type[TComponent]) -> Sequence[TComponent]:
        """
        관리하고 있는 Components를 반환합니다.
        :param _componentsType: 검색할 Component의 타입들.
        :return: 해당 타입의 Component들을 관리하고 있다면 해당 Component들의 인스턴스 List, 없다면 None.
        """
        return [self.__components[component] for component in _componentsType if component in self.__components]
    # endregion
    # region Life-Cycle
    def FixedUpdate(self) -> None:
        """
        고정된 주기마다 삭제할 Component가 있다면 삭제합니다.
        """
        if self.__components:
            toRemove: List[TComponent] = []
            for component in self.__components.values():
                if component.isDestroy:
                    key: Type[TComponent] = next(key for key, value in self.__components.items() if value is component)
                    toRemove.append(self.__components[key])

            for key in toRemove:
                self.__components.pop(key)
    # endregion