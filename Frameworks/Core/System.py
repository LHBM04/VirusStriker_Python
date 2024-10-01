from typing import final

from pico2d import *

from Level.LevelManagement import *
from Level.TestLevel import *
from Level.TestLevel import *

import Utilities.Singleton as Singleton
from Utilities.InputManagement import *
from Utilities.AudioManagement import *
from Utilities.ResourceManagement import *

@final
class SystemManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.windowName: str    = "Virus Striker"   # 프로그램(윈도우) 이름.
        self.windowWidth: int   = 1920              # 가로 해상도 (테스트).
        self.windowHeight: int  = 1080              # 세로 해상도 (테스트).
        self.isRunning: bool    = True              # 프로그램 구동 여부.
        self.gameFPS: float     = 0.0               # 게임 초당 프레임.

    def Inintialize(self) -> None:
        open_canvas(self.windowWidth, self.windowHeight) # 캔버스 열기
        SDL_SetWindowTitle(pico2d.window, self.windowName.encode('utf-8'))
        
        LevelManager().AddLevel("Test 1", TestLevel_1())
        LevelManager().AddLevel("Test 2", TestLevel_2())
    
        LevelManager().LoadLevel("Test 1")

    def Update(self, _deltaTime: float) -> None:
        LevelManager().Update(_deltaTime);
        InputManager().Update()
        #AudioManager().Update()
        
        if InputManager().GetKeyDown(SDLK_SPACE):
            SDL_SetWindowFullscreen(pico2d.window, SDL_WINDOW_FULLSCREEN_DESKTOP)

        if InputManager().GetKeyDown(SDLK_ESCAPE):
            self.isRunning = False

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        LevelManager().FixedUpdate(_fixedDeltaTime);

    def Render(self) -> None:
        clear_canvas()
        LevelManager().RenderObject();
        LevelManager().RenderUI();
        update_canvas()  # 캔버스 업데이트
    
    # 프로그램 종료 시 캔버스를 정리합니다.
    def CleanUp(self) -> None:
        clear_canvas()
        close_canvas()