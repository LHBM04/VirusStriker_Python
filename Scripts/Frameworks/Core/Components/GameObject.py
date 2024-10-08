from typing import final, List, Type, TypeVar

from Core.Components.Object import Object
class GameObject(Object):
    def __init__(self):
        super().__init__()

        from Core.Components.Component import ComponentManager
        from Core.Components.Transform import Transform

        self.__componentManager: ComponentManager = ComponentManager(self)
        self.__componentManager.AddComponent(Transform)

    #region [Properties]
    @property
    def transform(self) -> 'Transform':
        from Core.Components.Transform import Transform
        return self.__componentManager.GetComponent(Transform)

    @property
    def gameObject(self) -> 'GameObject':
        return self
    #endregion

    from Core.Components.Component import Component
    TComponent: TypeVar = TypeVar('TComponent', bound = Component)

    # region [Methods]
    # 관리 중인 Component를 가져옵니다
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__componentManager.GetComponent(_component)

        # 관리 중인 Component들을 가져옵니다.

    def GetComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return self.__componentManager.GetComponents(*_components)

        # 관리 중인 Component들을 가져옵니다.

    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__componentManager.AddComponent(_component)

        # 관리 중인 Component들을 가져옵니다.

    def AddComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return self.__componentManager.AddComponents(*_components)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehaviour(self, _behaviour: 'Behaviour') -> None:
        self.__behaviourManager.AddBehaviour(_behaviour)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehaviours(self, *_behaviours: 'Behaviour') -> None:
        self.__behaviourManage

@final
class GameObjectManager:
    def __init__(self):
        pass
