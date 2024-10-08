from abc import ABCMeta
from typing import final, Iterator, List, Type, TypeVar

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject


class Behavior(Component, metaclass = ABCMeta):
    def __init__(self, _actor: 'GameObject'):
        super().__init__(_actor)
        self.__actor: 'GameObject'  = _actor
        self.__isEnabled: bool      = True

    # region [Properties]
    @property
    def isEnabled(self) -> bool:
        return self.__isEnabled

    @isEnabled.setter
    def isEnabled(self, _enable: bool) -> None:
        if _enable:
            if self.__isEnabled:
                return

            self.__isEnabled = True
            self.OnEnable()
        else:
            if not self.__isEnabled:
                return

            self.__isEnabled = False
            self.OnDisable()
    # endregion
    def OnEnable(self) -> None:
        pass

    def OnStart(self) -> None:
        pass

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def Update(self, _deltaTime: float) -> None:
        pass

    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    def OnTriggerEnter2D(self) -> None:
        pass

    def OnTriggerStay2D(self) -> None:
        pass

    def OnTriggerExit2D(self) -> None:
        pass

    def OnCollisionEnter2D(self) -> None:
        pass

    def OnCollisionEixt2D(self) -> None:
        pass

    def OnDisable(self) -> None:
        pass

    def OnDestroy(self) -> None:
        pass

# 타입 검색을 위한 제너릭 타입 선언.
TBehavior: TypeVar = TypeVar('TBehaviour', bound = Behavior)

@final
class BehaviorManager:
    def __init__(self, _actor: 'GameObject'):
        self.__actor: GameObject               = _actor    # 액터
        self.__behaviours: List[TBehavior]     = []        # 관리 중인 Behaviour.
        self.__addBehaviours: List[TBehavior]  = []        # 추가할 Behaviour.

    # region [Operators Override]
    def __iter__(self) -> Iterator[TBehavior]:
        return iter(self.__behaviours)

    def __getitem__(self, index: int) -> TBehavior:
        return self.__behaviours[index]

    def __len__(self) -> int:
        return len(self.__behaviours)
        # endregion
        # region [Methods]

    def AddBehaviour(self, _behavior: Type[TBehavior]) -> TBehavior:
        newBehavior: TBehavior = _behavior(self.__actor)
        self.__addBehaviours.append(_behavior)

        return newBehavior

    def AddBehaviours(self, *_behaviors: Type[TBehavior]) -> List[TBehavior]:
        newBehaviors: List[TBehavior] = []
        for currentBehavior in _behaviors:
            if currentBehavior in self.__behaviours:
                continue

            newBehavior: TBehavior = currentBehavior(self.__actor)
            self.__addBehaviours.extend(newBehavior)
            newBehaviors.append(newBehavior)

        return newBehaviors
    # endregion