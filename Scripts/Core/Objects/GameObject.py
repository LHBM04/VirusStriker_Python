from typing import final, List, Iterator, Type, TypeVar, Sequence

from Core.Objects.Object import Object

class GameObject(Object):
    def __init__(self):
        super().__init__()

        from Core.Components.Component import ComponentManager
        from Core.Behaviors.Behavior import BehaviorManager
        from Core.Components.Transform import Transform

        self.__behaviorManager: BehaviorManager     = BehaviorManager(self)
        self.__componentManager: ComponentManager   = ComponentManager(self)
        self.__transform: Transform                 = self.__componentManager.AddComponent(Transform)
        self.__isActiveSelf: bool                   = True

    #region [Properties]
    @property
    def transform(self) -> 'Transform':
        return self.__transform

    @property
    def gameObject(self) -> 'GameObject':
        return self

    @property
    def isActiveSelf(self) -> bool:
        return self.__isActiveSelf

    @property
    def isActive(self) -> bool:
        if self.transform.parent:
            return self.__isActiveSelf and self.transform.parent.gameObject.isActiveSelf

        return self.__isActiveSelf
    #endregion
    def SetActive(self, _active: bool):
        self.__isActiveSelf = _active
        for behavior in self.__behaviorManager:
            behavior.isEnable = False

        if not self.__isActiveSelf:
            if len(self.transform.children) > 0:
                for child in self.transform.children:
                    child.gameObject.SetActive(_active)
    # region [Life-Cycle Methods]
    def Update(self, _deltaTime: float):
        if not self.__isActiveSelf:
            return

        self.__componentManager.Update(_deltaTime)
        self.__behaviorManager.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        if not self.__isActiveSelf:
            return

        self.__componentManager.FixedUpdate(_fixedDeltaTime)
        self.__behaviorManager.FixedUpdate(_fixedDeltaTime)

    def OnDestroy(self):
        map(lambda component: Object.Destroy(component), self.__componentManager)   # 컴포넌트 파괴
        map(lambda behavior: Object.Destroy(behavior), self.__behaviorManager)      # 행동 파괴
        map(lambda child : Object.Destroy(child), self.transform.children)          # 자식 파괴
    # endregion
    # region [Component Methods]
    from Core.Components.Component import Component
    TComponent: TypeVar = TypeVar('TComponent', bound=Component)

    # 관리 중인 Component를 가져옵니다
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__componentManager.GetComponent(_component)

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_components: Type[TComponent]) -> Sequence[TComponent]:
        return self.__componentManager.GetComponents(*_components)

    # 관리 중인 Component들을 가져옵니다.
    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__componentManager.AddComponent(_component)

    # 관리 중인 Component들을 가져옵니다.
    def AddComponents(self, *_components: Type[TComponent]) -> Sequence[TComponent]:
        return self.__componentManager.AddComponents(*_components)
    # endregion
    # region [Behaviors Method]
    from Core.Behaviors.Behavior import Behavior
    TBehavior: TypeVar = TypeVar('TBehavior', bound = Behavior)

    # 관리 중인 Component를 가져옵니다
    def GetCBehavior(self, _component: Type[TBehavior]) -> TBehavior:
        return self.__behaviorManager.GetBehavior(_component)

    # 관리 중인 Component들을 가져옵니다.
    def GetBehaviors(self, *_behaviors: Type[TBehavior]) -> Sequence[TBehavior]:
        return self.__behaviorManager.GetBehaviors(*_behaviors)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehavior(self, _behavior: Type[TBehavior]) -> TBehavior:
        return self.__behaviorManager.AddBehavior(_behavior)

    # 관리 중인 Component들을 가져옵니다.
    def AddBehaviors(self, *_behaviors: Type[TBehavior]) -> Sequence[TBehavior]:
        return self.__behaviorManager.AddBehaviors(*_behaviors)
    # endregion

@final
class GameObjectManager:
    def __init__(self):
        self.__gameObjects: List[GameObject]    = []
        self.__addGameObjects: List[GameObject] = []

    #region [Operators Override]
    def __iter__(self) -> Iterator[GameObject]:
        return iter(self.__gameObjects)

    def __getitem__(self, _index: int) -> GameObject:
        return self.__gameObjects[_index]

    def __len__(self) -> int:
        return len(self.__gameObjects)
    # endregion

    def AddGameObject(self, _gameObject: GameObject) -> None:
        self.__addGameObjects.append(_gameObject)

    # region [Life-Cycle Methods]
    def Update(self, _deltaTime: float):
        if self.__addGameObjects:
            self.__gameObjects.extend(self.__addGameObjects)
            self.__addGameObjects.clear()

        if self.__gameObjects:
            for currentObject in self.__gameObjects:
                currentObject.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        for currentObject in self.__gameObjects:
            currentObject.FixedUpdate(_fixedDeltaTime)

            if currentObject.isDestroy:
                index: int = self.__gameObjects.index(currentObject)
                self.__gameObjects.pop(index).OnDestroy()
    # endregion
    