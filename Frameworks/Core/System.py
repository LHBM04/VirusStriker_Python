from typing import final

from pico2d import *

from Core.Sprite import *
from Level.Scene import *

from Level.Scene import *
from Level.TestScenes import *
from Utilities.InputSystem import *
from Utilities.AudioSystem import *
from Utilities.Singleton import *
from Utilities.FileSystem import *

@final
class SystemManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.windowName: str    = "Virus Striker"   # 프로그램(윈도우) 이름.
        self.windowWidth: int   = 1280              # 가로 해상도 (테스트).
        self.windowHeight: int  = 800               # 세로 해상도 (테스트).
        self.isRunning: bool    = True              # 프로그램 구동 여부.
        self.gameFPS: float     = 0.0               # 게임 초당 프레임.

        
        open_canvas(self.windowWidth, 
                    self.windowHeight) # 캔버스 열기

    def Inintialize(self) -> None:
        LevelManager().AddLevel("Test 1", TestScene1())
        LevelManager().AddLevel("Test 2", TestScene2())

        LevelManager().LoadLevel("Test 1")

    def Update(self, _deltaTime: float) -> None:
        LevelManager().Update(_deltaTime);
        InputManager().Update()
        AudioManager().Update()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        LevelManager().FixedUpdate(_fixedDeltaTime);

    def Render(self) -> None:
        LevelManager().RenderObject();
        LevelManager().RenderUI();
    
    # 프로그램 종료 시 캔버스를 정리합니다.
    def CleanUp(self) -> None:
        clear_canvas()
        close_canvas()