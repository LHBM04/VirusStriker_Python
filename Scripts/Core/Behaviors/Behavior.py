from abc import ABCMeta, abstractmethod
from typing import final, Iterator, Iterable, List, Dict, Type, TypeVar

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject

class Behavior(Component, metaclass = ABCMeta):
    """
    Game Object의 행동, 흐름을 관리하고 제어합니다.
    """
    def __init__(self, _actor: GameObject):
        super().__init__(_actor)

        self.__isEnabled: bool = True

    # region Properties
    @property
    def isEnable(self) -> bool:
        """
        해당 Behavior가 활성화되어 있는지에 대한 여부를 반환합니다.
        :return: 해당 Behavior가 활성화되어 있는지에 대한 여부.
        """
        return self.__isEnabled

    @isEnable.setter
    def isEnable(self, _enable: bool) -> None:
        """
        해당 Behavior의 활성화 여부를 설정합니다.
        :param _enable: 해당 Behavior의 활성화 여부.
        """
        if _enable and not self.__isEnabled:
            self.__isEnabled = True
            self.OnEnable()
        elif not _enable and self.__isEnabled:
            self.__isEnabled = False
            self.OnDisable()

    @property
    def isActiveAndEnabled(self) -> bool:
        """
        해당 Behavior와 이를 수행하는 Game Object의 활성화 여부를 같이 반환합니다.
        :return: 해당 Behavior와 이를 수행하는 Game Object의 활성화 여부.
        """
        return self.__isEnabled and self.gameObject.isActive
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self):
        super().Start()

    @abstractmethod
    def OnEnable(self) -> None:
        """
        해당 Behavior가 활성화되었을 때 한번 실행됩니다.
        """
        pass

    @abstractmethod
    def Update(self, _deltaTime: float):
        """
        해당 Behavior의 동작을 매 프레임 갱신합니다.\n
        (※ 게임 루프 내에서 매 프레임 호출됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float):
        """
        해당 Behavior의 물리 연산과 같은 고정된 주기의 업데이트를 처리합니다.\n
        (※ 물리 연산이나 시간에 의존적인 처리는 이 메서드에서 처리됩니다.)
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def LateUpdate(self, _deltaTime: float):
        """
        해당 Behavior의 동작을 매 프레임 갱신합니다.\n
        (※ Update() 이후 실행됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def OnDisable(self) -> None:
        """
        해당 Behavior가 비활성화되었을 때 한번 실행됩니다.
        """
        pass

    @abstractmethod
    def OnDestroy(self):
        """
        해당 Behavior가 파괴되었을 때 한번 실행됩니다.
        (※ 해당 Behavior를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        :return:
        """
        super().OnDestroy()
    # endregion

# 제네릭(Behavior를 상속받은 클래스만 가능하게끔 제한).
TBehavior: TypeVar = TypeVar('TBehavior', bound = Behavior)

@final
class BehaviorController:
    """
    Game Object에 추가되어 있는 모든 Behavior를 제어합니다.
    """
    def __init__(self, _actor: GameObject):
        self.__actor: GameObject                             = _actor   # 해당 Controller의 주인(Owner).
        self.__behaviors: Dict[Type[TBehavior], TBehavior]   = {}       # 관리하고 있는 모든 Component.

    # region Operators Override
    def __iter__(self) -> Iterator[TBehavior]:
        """
        관리하는 모든 Behavior를 순회할 수 있도록 Iterator를 반환합니다.
        :return: 관리하고 있는 모든 Behavior에 대한 Iterator.
        """
        return iter(self.__behaviors.values())

    def __getitem__(self, _index: Type[TBehavior]) -> TBehavior:
        """
        인덱스를 통해 특정 Behavior를 가져옵니다.
        :param _index: 가져올 Behavior의 타입.
        :return: 해당 타입의 Behavior 인스턴스.
        """
        return self.GetBehavior(_index)

    def __len__(self) -> int:
        """
        관리하고 있는 모든 Behavior의 수를 반환합니다.
        :return: Behavior의 개수.
        """
        return len(self.__behaviors)
    # endregion
    # region Management Methods
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
    # region Life-Cycle
    def Update(self, _deltaTime: float):
        """
        매 프레임마다 관리하는 모든 Behavior를 업데이트합니다.
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

    def FixedUpdate(self, _fixedDeltaTime: float):
        """
        고정된 주기마다 모든 Behavior의 물리 연산를 처리합니다.\n
        또한, 삭제할 Behavior가 있다면 삭제합니다.
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 간격(초 단위).
        """
        removeBehaviors: List[Type[TBehavior]] = []
        if self.__behaviors:
            for behavior in self.__behaviors.values():
                if behavior.isEnable:
                    behavior.FixedUpdate(_fixedDeltaTime)

                if behavior.isDestroy:
                    removeBehaviors.append(Type[behavior])

        if removeBehaviors:
            for removeBehavior in removeBehaviors:
                self.__behaviors.pop(removeBehavior).OnDestroy()
    # endregion