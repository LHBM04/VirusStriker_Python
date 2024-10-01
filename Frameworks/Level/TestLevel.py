from Core.System import *
from Core.Actors.Player import *
from Level.LevelManagement import *
from Utilities.InputManagement import *

class TestLevel_1(Level):
    def __init__(self, _levelName: str = "Test Level 1") -> None:
        super().__init__(_levelName)
        # 테스트 백그라운드
        self.background: Object = Object();
        
        self.background.position = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.background.scale = Vector2(1.0, 1.0)
        
        self.background.sprite = Sprite(self.background, "Resources\\Sprites\\Backgrounds\\Stages\\Stage 1")
        self.background.sprite.info.layerLevel = Sprite.Info.ELevel.BACKGROUND
        self.background.sprite.info.renderLayer = 0
        
        # 테스트 플레이어
        self.testPlayer: Player = Player()
        self.testPlayer.position = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)

    def OnEnter(self) -> None:
        self.objectManager.AddObject(self.background)
        self.objectManager.AddObject(self.testPlayer)

        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyDown(SDLK_RETURN):
            LevelManager().LoadLevel("Test 2")

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnRender(self) -> None:
        self.objectManager.Render()
    
    def OnUIRender(self) -> None:
        pass

    def OnExit(self) -> None:
        self.objectManager.ClearObjects()
        self.uiManager.ClearObjects()

        print(f"Good bye, This is {self.levelName}!")

class TestLevel_2(Level):
    def __init__(self, _levelName: str = "Test Level 2") -> None:
        super().__init__(_levelName)

    def OnEnter(self) -> None:
        print(f"Hello, This is {self.levelName}!")

    def OnUpdate(self, _deltaTime: float) -> None:
        if InputManager().GetKeyDown(SDLK_BACKSPACE):
            LevelManager().UnloadLevel()

    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    def OnRender(self) -> None:
        pass
    
    def OnUIRender(self) -> None:
        pass

    def OnExit(self) -> None:
        self.objectManager.ClearObjects()
        self.uiManager.ClearObjects()

        print(f"Good bye, This is {self.levelName}!")