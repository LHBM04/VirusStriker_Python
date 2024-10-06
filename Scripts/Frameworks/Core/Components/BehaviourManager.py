from typing import final, Iterator, List
from typing import Type, TypeVar

from Core.Components.Behaviour import Behaviour
from Core.Components.GameObject import GameObject

# 타입 검색을 위한 제너릭 타입 선언.
TBehaviour: TypeVar = TypeVar('TBehaviour', bound = Behaviour)

@final
class BehaviourManager:
    def __init__(self, _actor: GameObject):
        self.__behaviours: List[TBehaviour]      = []    # 관리 중인 Behaviour.
        self.__addBehaviours: List[TBehaviour]   = []    # 추가할 Behaviour.

    # [Operators Override] #
    def __iter__(self) -> Iterator[TBehaviour]:
        return iter(self.__behaviours)

    def __getitem__(self, index: int) -> TBehaviour:
        return self.__behaviours[index]

    def __len__(self) -> int:
        return len(self.__behaviours)

    # [Methods] #
    def AddBehaviour(self, _behaviour: TBehaviour) -> None:
        self.__addBehaviours.append(_behaviour)

    def AddBehaviours(self, *_behaviours: TBehaviour) -> None:
        self.__addBehaviours.extend(_behaviours)