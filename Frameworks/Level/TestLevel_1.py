from Core.System import *
from Core.Actors.TestObject import *
from Level.LevelManagement import *
from Utilities.InputManagement import *

class TestLevel_1(Level):
    def __init__(self, _levelName: str = "Test Level 1") -> None:
        super().__init__(_levelName)

        self.m_objectManager.AddObject(TestPlayer())

    def OnEnter(self) -> None:
        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_RETURN) is EInputState.DOWN:
            LevelManager().LoadScene("Test 2")

        if InputManager().GetKeyState(SDLK_ESCAPE) == EInputState.DOWN:
            SystemManager().isRunning = False

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnRender(self) -> None:
        self.m_objectManager.Render()
    
    def OnUIRender(self) -> None:
        pass

    def OnExit(self) -> None:
        self.m_objectManager.ClearObjects()
        self.m_uiManager.ClearObjects()

        print(f"Good bye, This is {self.levelName}!")
