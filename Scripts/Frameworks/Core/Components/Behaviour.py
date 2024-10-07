from abc import ABCMeta
from typing import final, Iterator, List, TypeVar

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject

class Behaviour(Component, metaclass = ABCMeta):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)
        self.__isEnabled: bool = True
    #region [Properties]
    @property
    def isEnabled(self) -> bool:
        return self.__isEnabled
    #endregion
    #region [Methods]
    def FixedUpdate(self, _fixedDeltaTime: float):
        if not self.isEnabled:
            return

        self.OnFixedUpdate(_fixedDeltaTime)

    def Update(self, _deltaTime: float):
        if not self.isEnabled:
            return

        self.OnUpdate(_deltaTime)

    def LateUpdate(self, _deltaTime: float):
        if not self.isEnabled:
            return

        self.OnLateUpdate(_deltaTime)
    #endregion
    #region [Life-Cycle Methods]
    def OnEnabled(self) -> None:
        pass

    def OnStart(self) -> None:
        pass

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    def OnLateUpdate(self, _deltaTime: float) -> None:
        pass

    def OnDisable(self) -> None:
        pass

    def OnDestroy(self) -> None:
        pass
    #endregion

# 타입 검색을 위한 제너릭 타입 선언.
TBehaviour: TypeVar = TypeVar('TBehaviour', bound = Behaviour)

@final
class BehaviourManager:
    def __init__(self, _actor: GameObject):
        self.__behaviours: List[TBehaviour]      = []    # 관리 중인 Behaviour.
        self.__addBehaviours: List[TBehaviour]   = []    # 추가할 Behaviour.

    #region [Operators Override]
    def __iter__(self) -> Iterator[TBehaviour]:
        return iter(self.__behaviours)

    def __getitem__(self, index: int) -> TBehaviour:
        return self.__behaviours[index]

    def __len__(self) -> int:
        return len(self.__behaviours)
    #endregion
    #region [Methods]
    def AddBehaviour(self, _behaviour: TBehaviour) -> None:
        self.__addBehaviours.append(_behaviour)

    def AddBehaviours(self, *_behaviours: TBehaviour) -> None:
        self.__addBehaviours.extend(_behaviours)
    #endregion