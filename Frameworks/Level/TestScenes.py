import Level.Scene
from Core.Actors.TestObject import *
from Level.Scene import *
from Utilities.InputSystem import *

class TestScene1(Level):
    def __init__(self, _levelName: str = "Test Level 1") -> None:
        super().__init__(_levelName)

        self.m_objectManager.AddObject(TestObject())

    def OnEnter(self) -> None:
        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_RETURN) is EInputState.DOWN:
            LevelManager().LoadScene("Test 2")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        print(f"Good bye, This is {self.levelName}!")

class TestScene2(Level):
    def __init__(self, _levelName: str = "Test Level 2") -> None:
        super().__init__(_levelName)

    def OnEnter(self) -> None:
        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_BACKSPACE) == EInputState.DOWN:
            LevelManager().UnloadScene()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        print(f"Good bye, This is {self.levelName}!")
