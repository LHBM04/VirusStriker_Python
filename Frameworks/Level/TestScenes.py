import Level.Scene
from Level.Scene import *
from Utilities.InputSystem import *

class TestScene1(Scene):
    def __init__(self, _sceneName: str = "Test Scene 1") -> None:
        super().__init__(_sceneName)
        self.m_timer: float = 0.0

    def OnEnter(self) -> None:
        print(f"Hello, World! This is Test Scene 1!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_RETURN) is EInputState.DOWN:
            SceneManager().LoadScene("Test 2")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

class TestScene2(Scene):
    def __init__(self, _sceneName: str = "Test Scene 2") -> None:
        super().__init__(_sceneName)

    def OnEnter(self) -> None:
        print(f"Hello, World! This is Test Scene 2!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyState(SDLK_RETURN) == EInputState.DOWN:
            SceneManager().LoadScene("Test 1")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        print(f"Fixed Update on Test Scene 2")
