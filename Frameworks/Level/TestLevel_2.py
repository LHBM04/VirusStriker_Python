from Level.Level import *
from Utilities.InputSystem import *

class TestLevel_2(Level):
    def __init__(self, _levelName: str = "Test Level 2") -> None:
        super().__init__(_levelName)

    def OnEnter(self) -> None:
        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_BACKSPACE) == EInputState.DOWN:
            LevelManager().UnloadScene()

    def OnExit(self) -> None:
        self.m_objectManager.ClearObjects()
        self.m_uiManager.ClearObjects()

        print(f"Good bye, This is {self.levelName}!")
