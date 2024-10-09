from abc import ABCMeta
from typing import final, Iterator, List, Dict, Type, TypeVar

from Core.Components.Object import Object

class Component(Object, metaclass = ABCMeta):
    def __init__(self, _owner: 'GameObject'):
        super().__init__()

        from Core.Components.GameObject import GameObject
        self.__owner: GameObject    = _owner
        self.__isActive: bool       = True

    #region [Properties]
    @property
    def name(self) -> str:
        return self.__owner.name

    @name.setter
    def name(self, _name) -> None:
        self.__owner.name = _name

    @property
    def gameObject(self) -> 'GameObject':
        return self.__owner

    @property
    def transform(self) -> 'Transform':
        return self.__owner.transform

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, _active) -> None:
        self.SetActive(_active)
    #endregion
    def OnEnable(self) -> None:
        pass

    def OnDisable(self) -> None:
        pass

    def SetActive(self, _active) -> None:
        if _active:
            self.__isActive = True
            self.OnEnable()
        else:
            self.__isActive = False
            self.OnDisable()

# 타입 검색을 위한 제너릭 타입 선언.
TComponent: TypeVar = TypeVar('TComponent', bound = Component)

@final
class ComponentManager:
    def __init__(self, _owner: 'GameObject'):
        self.__owner                                                = _owner
        self.__components: Dict[Type[TComponent], TComponent]       = {}
        self.__addComponents: Dict[Type[TComponent], TComponent]    = {}

    #region [Properties]
    @property
    def gameObject(self) -> 'GameObject':
        return self.__owner

    @property
    def transform(self) -> 'Transform':
        return self.__owner.transform
    #endregion
    #region [Operators Override]
    def __iter__(self) -> Iterator[TComponent]:
        return iter(self.__components)

    def __getitem__(self, _index: Type[TComponent]) -> TComponent:
        return self.GetComponent(_index)

    def __len__(self) -> int:
        return len(self.__components)
    #endregion
    #region [Methods]
    # 관리 중인 Component를 가져옵니다.
    def GetComponent(self, _component: Type[TComponent]) -> TComponent:
        return self.__components[_component] if _component in self.__components.keys() else None

    # 관리 중인 Component들을 가져옵니다.
    def GetComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        return [self.__components[component] for component in _components if component in self.__components]

    def AddComponent(self, _component: Type[TComponent]) -> TComponent:
        if _component in self.__components:
            raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {type(_component)}")

        newComponent: TComponent = _component(self.__owner)
        self.__addComponents[_component] = newComponent
        newComponent.Start()
        return newComponent

    def AddComponents(self, *_components: Type[TComponent]) -> List[TComponent]:
        newComponents: List[TComponent] = []
        for currentComponent in _components:
            if currentComponent in self.__components:
                raise ValueError(f"[Oops!] 중복된 Component는 허용하지 않습니다! {currentComponent}")
            else:
                newComponent: TComponent = currentComponent(self.__owner)
                self.__addComponents[currentComponent] = newComponent
                newComponents.append(newComponent)
                newComponents[-1].Start()

        return newComponents
    # endregion
    # region [Life-Cycle Methods]
    def Update(self, _deltaTime: float):
        # 새로운 컴포넌트 추가
        if len(self.__addComponents) > 0:
            self.__components.update(self.__addComponents)
        
        # 컴포넌트 Update.
        if len(self.__components) > 0:
            for currentComponent in self.__components:
                if currentComponent.isActive:
                    currentComponent.Update(_deltaTime)

        # 컴포넌트 LateUpdate.
        if len(self.__components) > 0:
            for currentComponent in self.__components:
                if currentComponent.isActive:
                    currentComponent.LateUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        # 컴포넌트 FixedUpdate.
        for currentComponent in self.__components:
            if currentComponent.isActive:
                currentComponent.FixedUpdate(_fixedDeltaTime)

            # 컴포넌트 Destroy.
            if currentComponent.isDestroy:
                self.__components.pop(currentComponent).OnDestroy()

    def Render(self):
        if len(self.__components) > 0:
            for currentComponent in self.__components:
                if currentComponent.isActive:
                    currentComponent.Render()

    def RenderDebug(self):
        if len(self.__components) > 0:
            for currentComponent in self.__components:
                if currentComponent.isActive:
                    currentComponent.RenderDebug()
    # endregion
