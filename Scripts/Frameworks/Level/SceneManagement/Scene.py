from abc import ABCMeta, abstractmethod

class Scene(metaclass = ABCMeta):
    def __init__(self):
        self.name = "New Scene"

    # [virtual methods] #
    def Update(self, _deltaTime: float) -> None:
        self.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self) -> None:
        self.OnRenderObject()

    def RenderUI(self) -> None:
        self.OnRenderGUI()

    # [abstract methods] #
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
    def OnExit(self) -> None:
        pass

    @abstractmethod
    def OnRenderObject(self) -> None:
        pass

    @abstractmethod
    def OnRenderGUI(self) -> None:
        pass