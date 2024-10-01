from abc import ABC, abstractmethod

from Frameworks.Core.GameObject import ObjectManager

class Scene(ABC):
    def __init__(self) -> None:
        self.objectManager: ObjectManager = ObjectManager()   # 해당 Level 내 오브젝트를 관리하는 매니저 인스턴스
        self.uiManager: ObjectManager = ObjectManager()   # 해당 Level 내 UI를 관리하는 매니저 인스턴스

    # -------------------[virtual methods]------------------- #

    def Update(self, _deltaTime: float) -> None:
        self.objectManager.Update(_deltaTime)
        self.uiManager.Update(_deltaTime)

        self.OnUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.objectManager.FixedUpdate(_fixedDeltaTime)
        self.uiManager.FixedUpdate(_fixedDeltaTime)

        self.OnFixedUpdate(_fixedDeltaTime)

    def RenderObject(self) -> None:
        self.objectManager.Render()
        self.OnRender()

    def RenderUI(self) -> None:
        self.uiManager.Render()
        self.OnUIRender()

    # -------------------[abstract methods]------------------- #

    @abstractmethod
    def OnEnter(self) -> None:
        pass

    @abstractmethod
    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    @abstractmethod
    def OnRender(self) -> None:
        pass

    @abstractmethod
    def OnUIRender(self) -> None:
        pass

    @abstractmethod
    def OnExit(self) -> None:
        pass