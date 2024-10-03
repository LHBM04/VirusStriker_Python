from typing import final

from Level.SceneManagement import Scene


@final
class OpeningScene(Scene):
    def __init__(self):
        super().__init__()

    def OnEnter(self) -> None:
        print("Hello!")

    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()

class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def OnEnter(self) -> None:
        pass

    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnExit(self) -> None:
        pass

    def OnRender(self) -> None:
        super().OnRender()

    def OnUIRender(self) -> None:
        super().OnUIRender()