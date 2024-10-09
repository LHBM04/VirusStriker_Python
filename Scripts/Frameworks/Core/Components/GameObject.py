from typing import final, List, Iterator, Type, TypeVar

from Core.Components.Object import Object

class GameObject(Object):
    def __init__(self):
        super().__init__()

        from Core.Components.Component import ComponentManager
        from Core.Components.Transform import Transform

        self.__componentManager: ComponentManager   = ComponentManager(self)
        self.__transform: Transform                 = self.__componentManager.AddComponent(Transform)
        self.__isActive: bool                       = True

    #region [Properties]
    @property
    def transform(self) -> 'Transform':
        return self.__transform

    @property
    def gameObject(self) -> 'GameObject':
        return self
    #endregion
    # region [Life-Cycle Methods]
    def Update(self, _deltaTime: float):
        super().Update(_deltaTime)
        self.__componentManager.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        super().FixedUpdate(_fixedDeltaTime)
        self.__componentManager.FixedUpdate(_fixedDeltaTime)

    def Render(self):
        super().Render()
        self.__componentManager.Render()

    def RenderDebug(self):
        super().RenderDebug()
        self.__componentManager.RenderDebug()
    # endregion
    # region [Component Methods]
    from Core.Components.Component import Component
    TComponent: TypeVar = TypeVar('TComponent', bound=Component)

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
        _gameObject.Start()

    # region [Life-Cycle Methods]
    def Update(self, _deltaTime: float):
        # 새로운 컴포넌트 추가
        if len(self.__addGameObjects) > 0:
            self.__gameObjects.extend(self.__addGameObjects)

        # 컴포넌트 Update.
        if len(self.__gameObjects) > 0:
            for currentObject in self.__gameObjects:
                currentObject.Update(_deltaTime)

        # 컴포넌트 LateUpdate.
        if len(self.__gameObjects) > 0:
            for currentObject in self.__gameObjects:
                currentObject.LateUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        # 컴포넌트 FixedUpdate.
        for currentObject in self.__gameObjects:
            currentObject.FixedUpdate(_fixedDeltaTime)

            # 컴포넌트 Destroy.
            if currentObject.isDestroy:
                index: int = self.__gameObjects.index(currentObject)
                self.__gameObjects.pop(index).OnDestroy()

    def Render(self):
        if len(self.__gameObjects) > 0:
            for currentObject in self.__gameObjects:
                currentObject.Render()

    def RenderDebug(self):
        if len(self.__gameObjects) > 0:
            for currentObject in self.__gameObjects:
                currentObject.RenderDebug()
    # endregion
    