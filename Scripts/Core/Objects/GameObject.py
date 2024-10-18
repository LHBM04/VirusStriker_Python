from __future__ import annotations
from abc import abstractmethod
from typing import Dict, Iterable, List, Type, TypeVar

from Core.Behaviors.Behavior import Behavior
from Core.Components.Component import Component
from Core.Objects.Object import Object

# 제네릭 타입(Component를 상속받은 클래스만 가능하게끔 제한).
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

# 제네릭 타입(Behavior를 상속받은 클래스만 가능하게끔 제한).
TBehavior: TypeVar = TypeVar('TBehavior', bound = Behavior)

class GameObject(Object):
    """
    게임 내 사용될 객체입니다.\n
    (예: 플레이어, 적군, 아이템 등)
    """
    def __init__(self):
        super().__init__()
        self.__isActiveSelf: bool = True

        self.__components: Dict[Type[TComponent], TComponent] = {}
        self.__behaviors: Dict[Type[TBehavior], TBehavior]    = {}

    # region Properties
    @property
    def gameObject(self) -> GameObject:
        """
        해당 Game Object 자신을 반환합니다.
        :return: 해당 Game Object 자기 자신.
        """
        return self

    @property
    def transform(self) -> 'Transform':
        """
        해당 Game Object의 Transform을 반환합니다.
        :return: 해당 Game Object의 Transform.
        """
        from Core.Components.Transform import Transform
        return self.GetComponent(Transform)

    def renderer(self) -> 'SpriteRenderer':
        from Core.Components.SpriteRenderer import SpriteRenderer
        return self.GetComponent(SpriteRenderer)

    @property
    def isActiveSelf(self) -> bool:
        """
        해당 Game Object가 활성화 되어 있는지에 대한 여부를 반환합니다.
        :return: 해당 Game Object의 활성화 여부.
        """
        return self.__isActiveSelf

    @property
    def isActive(self) -> bool:
        """
        부모 Game Object를 비롯하여, 자기 자신이 활성화 되어 있는지에 대한 여부를 반환합니다.
        :return: 부모 Game Object를 비롯하여, 자기 자신이 활성화 되어 있는지에 대한 여부.
        """
        return self.__isActiveSelf
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self) -> None:
        """
        해당 Game Object가 탄생했을 때 한번 실행됩니다.
        (※ 해당 Game Object를 관리하는 Controller/Manager에 추가된 시점을 의미합니다.)
        """
        pass

    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        """
        해당 Game Object의 상태를 매 프레임 갱신합니다.
        (※ 게임 루프 내에서 매 프레임 호출됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 간격(초 단위).
        """
        if self.__behaviors:
            for behavior in self.__behaviors.values():
                if behavior.isEnable:
                    behavior.Update(_deltaTime)

        if self.__behaviors:
            for behavior in self.__behaviors.values():
                if behavior.isEnable:
                    behavior.LateUpdate(_deltaTime)

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        """
        해당 Game Object의 물리 연산과 같은 고정된 주기의 업데이트를 처리합니다.\n
        (※ 물리 연산이나 시간에 의존적인 처리는 이 메서드에서 처리됩니다.)
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 간격(초 단위).
        """
        if self.__components:
            toRemove: List[TComponent] = []
            for component in self.__components.values():
                if component.isDestroy:
                    toRemove.append(self.__components[type(component)])

            for key in toRemove:
                self.__components.pop(type(key))

        if self.__behaviors:
            toRemove: List[TBehavior] = []
            for behavior in self.__behaviors.values():
                if behavior.isEnable:
                    behavior.FixedUpdate(_fixedDeltaTime)

                if behavior.isDestroy:
                    toRemove.append(Type[behavior])

            if toRemove:
                for behavior in toRemove:
                    self.__behaviors.pop(type(behavior)).OnDestroy()

    @abstractmethod
    def OnDestroy(self) -> None:
        """
        해당 Game Object가 파괴될 때 한번 실행됩니다.\n
        (※ 해당 Game Object를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        map(lambda component: Object.Destroy(component), self.__components)    # 컴포넌트 파괴
        map(lambda behavior: Object.Destroy(behavior), self.__behaviors)       # 행동 파괴
        map(lambda child: Object.Destroy(child), self.transform.children)               # 자식 파괴
    # endregion
    # region Component Managmements
    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        """
        새로운 Component를 추가합니다.\n
        (※ 중복되는 Component는 허용하지 않습니다.)
        :param _component: 추가할 Component의 타입.
        :return: 추가한 Component의 인스턴스.
        """
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        self.__components[_component] = _component(self)
        return self.__components[_component]

    def AddComponents(self, *_components: Type[TComponent]) -> Iterable[TComponent]:
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
                self.__components[currentComponent] = currentComponent(self)
                newComponents.append(self.__components[currentComponent])

        return newComponents

    def RemoveComponent(self, _componentType: Type[TComponent]) -> bool:
        """
        관리 중인 Component를 삭제합니다.
        :param _componentType: 삭제할 Component의 타입.
        :return: 삭제 여부.
        """
        if _componentType not in self.__components:
            raise KeyError(f"[Oops!] 해당 Behavior는 존재하지 않습니다! 삭제하려던 타입은 \"{_componentType}\"였습니다.")

        self.__behaviors[_componentType].isDestroy = True
        return True

    def RemoveComponents(self, *_componentTypes: Type[TComponent]) -> bool:
        """
        관리 중인 Component들을 삭제합니다.
        :param _componentTypes: 삭제할 Component의 타입들.
        :return: 삭제 여부.
        """
        condition: bool = False
        for componentType in _componentTypes:
            if componentType in self.__components:
                condition = self.RemoveComponent(componentType)

        return condition

    def GetComponent(self, _componentType: Type[TComponent]) -> TComponent:
        """
        관리하고 있는 Component를 반환합니다.
        :param _componentType: 검색할 Component의 타입.
        :return: 해당 타입의 Component를 관리하고 있다면 해당 Component의 인스턴스, 없다면 None.
        """
        return self.__components[_componentType] if _componentType in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_componentsType: Type[TComponent]) -> Iterable[TComponent]:
        """
        관리하고 있는 Components를 반환합니다.
        :param _componentsType: 검색할 Component의 타입들.
        :return: 해당 타입의 Component들을 관리하고 있다면 해당 Component들의 인스턴스 List, 없다면 None.
        """
        return [self.__components[component] for component in _componentsType if component in self.__components]
    # endregion
    # region Behavior Managements
    def AddBehavior(self, _behaviorType: Type[TBehavior]) -> TBehavior:
        """
        새로운 Behavior를 추가합니다.\n
        (※ 중복되는 Behavior는 허용하지 않습니다.)
        :param _behaviorType: 추가할 Behavior의 타입.
        :return: 추가한 Behavior의 인스턴스.
        """
        if _behaviorType in self.__behaviors:
            raise ValueError(f"[Oops!] 중복된 Behavior는 허용하지 않습니다! 추가하려던 \"{_behaviorType}\"였습니다.")

        self.__behaviors[_behaviorType] = _behaviorType(self.__actor)
        self.__behaviors[_behaviorType].isEnable = True
        self.__behaviors[_behaviorType].Start()
        return self.__behaviors[_behaviorType]

    def AddBehaviors(self, *_behaviorTypes: Type[TBehavior]) -> Iterable[TBehavior]:
        """
        새로운 Behavior들을 추가합니다.\n
        (※ 중복되는 Behavior는 허용하지 않습니다.)
        :param _behaviorTypes: 추가할 Behavior들의 타입.
        :return: 추가한 Behavior들.
        """
        newBehaviors: List[TBehavior] = []
        for currentBehavior in _behaviorTypes:
            newBehaviors.append(self.AddBehavior(currentBehavior))

        return newBehaviors

    def RemoveBehavior(self, _behaviorType: Type[TBehavior]) -> bool:
        """
        특정 Behavior를 삭제합니다.
        :param _behaviorType: 삭제할 Behavior의 타입.
        :return: 삭제 여부.
        """
        if _behaviorType not in self.__behaviors:
            raise KeyError(f"[Oops!] 해당 Behavior는 존재하지 않습니다! 삭제하려던 타입은 \"{_behaviorType}\"였습니다.")

        self.__behaviors[_behaviorType].isDestroy = True
        return True

    def RemoveBehaviors(self, *_behaviors: Type[TBehavior]) -> bool:
        """
        특정 Behavior들을 삭제합니다.
        :param _behaviors: 삭제할 Behavior의 타입들.
        :return: 삭제 여부.
        """
        condition: bool = False
        for behavior in _behaviors:
            if behavior in self.__behaviors:
                condition = self.RemoveBehavior(behavior)

        return condition

    def GetBehavior(self, _behaviorType: Type[TBehavior]) -> TBehavior:
        """
        특정 Behavior를 반환합니다.
        :param _behaviorType: 검색할 Behavior의 타입.
        :return: 검색한 Behavior
        """
        if _behaviorType not in self.__behaviors:
            raise KeyError(f"[Oops!] 해당 Behavior는 존재하지 않습니다! 검색하려던 타입은 \"{_behaviorType}\"였습니다.")

        return self.__behaviors[_behaviorType]

    def GetBehaviors(self, *_behaviorTypes: Type[TBehavior]) -> Iterable[TBehavior]:
        """
        특정 Behavior들을 반환합니다.
        :param _behaviorTypes: 검색할 Behavior의 타입들.
        :return: 검색한 Behavior들.
        """
        newBehavior: List[TBehavior] = []
        for currentBehavior in _behaviorTypes:
            newBehavior.append(self.GetBehavior(currentBehavior))

        return newBehavior
    # endregion