import Level.Scene
from Core.Actors.TestObject import *
from Level.Scene import *
from Utilities.InputSystem import *

class TestScene1(Scene):
    def __init__(self, _sceneName: str = "Test Scene 1") -> None:
        super().__init__(_sceneName)

        self.m_objectManager.AddObject(TestObject())

    def OnEnter(self) -> None:
        print(f"Hello, World! This is {self.sceneName}")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_RETURN) is EInputState.DOWN:
            SceneManager().LoadScene("Test 2")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

class TestScene2(Scene):
    def __init__(self, _sceneName: str = "Test Scene 2") -> None:
        super().__init__(_sceneName)

    def OnEnter(self) -> None:
        print(f"Hello, World! This is {self.sceneName}")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_BACKSPACE) == EInputState.DOWN:
            SceneManager().UnloadScene()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        print(f"Fixed Update on Test Scene 2")
