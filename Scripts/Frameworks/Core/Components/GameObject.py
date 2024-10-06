from typing import List, Type, TypeVar

from Core.Components.Behaviour import Behaviour, BehaviourManager
from Core.Components.Component import Component, ComponentManager
from Core.Components.Object import Object
from Core.Components.Transform import Transform

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

class GameObject(Object):
    def __init__(self):
       super().__init__()
       self.name = "New Game Object"

       self.__componentManager: ComponentManager = ComponentManager(self)   # 해당 Object가 가지고 있는 Component.
       self.__behaviourManager: BehaviourManager = BehaviourManager(self)   # 해당 Object가 수행할 Behaviour.
       self.__componentManager.AddComponent(Transform)                      # Game Object는 기본적으로 Transform을 포함합니다.

    # [Properties] #
    @property
    def transform(self) -> Transform:
        return self.__componentManager.GetComponent(Transform)

    @property
    def gameObject(self) -> 'GameObject':
        return self

    # [Utilities] #
    # 관리 중인 Component를 가져옵니다
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__componentManager.GetComponent(_component)

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return self.__componentManager.GetComponents(*_components)

    # 관리 중인 Component들을 가져옵니다.
    def AddComponent(self, _component: Type[TComponent]) -> bool:
        return self.__componentManager.AddComponent(_component)

    # 관리 중인 Component들을 가져옵니다.
    def AddComponents(self, *_components: Type[TComponent]) -> bool:
        return self.__componentManager.AddComponents(*_components)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehaviour(self, _behaviour: Behaviour) -> None:
        self.__behaviourManager.AddBehaviour(_behaviour)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehaviours(self, *_behaviours: Behaviour) -> None:
        self.__behaviourManager.AddBehaviours(*_behaviours)