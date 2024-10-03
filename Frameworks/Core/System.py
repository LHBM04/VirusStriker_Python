from typing import final

from pico2d import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.InputManagement import InputManager
from Level.SceneManagement import SceneManager
from Level.Stages import OpeningScene
from Level.Stages import TitleScene


@final
class SystemManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.windowName: str    = "Virus Striker"   # 프로그램(윈도우) 이름.
        self.windowWidth: int   = 1280              # 가로 해상도 (테스트).
        self.windowHeight: int  = 800               # 세로 해상도 (테스트).
        self.isRunning: bool    = True              # 프로그램 구동 여부.
        self.gameFPS: float     = 0.0               # 게임 초당 프레임.
        self.m_fpsDeltaTime: float = 0.0
        self.fpsRate            = 60

    def Inintialize(self) -> None:
        open_canvas(self.windowWidth, self.windowHeight, False, False) # 캔버스 열기
        SDL_SetWindowTitle(pico2d.window, self.windowName.encode('utf-8'))      # 윈도우 이름 변경

        SceneManager().AddLevel("Opening Scene", OpeningScene())
        SceneManager().AddLevel("Title Scene", TitleScene())
        SceneManager().LoadLevel("Opening Scene")

        self.Render()

    def Update(self, _deltaTime: float) -> None:
        SceneManager().Update(_deltaTime);
        InputManager().Update()
        #AudioManager().Update()

        if InputManager().GetKeyDown(SDLK_SPACE):
            SDL_SetWindowFullscreen(pico2d.window, SDL_WINDOW_FULLSCREEN_DESKTOP)

        if InputManager().GetKeyDown(SDLK_ESCAPE):
            self.isRunning = False

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        SceneManager().FixedUpdate(_fixedDeltaTime)

    def Render(self) -> None:
        update_canvas()  # 캔버스 업데이트
        SceneManager().RenderObject()
        SceneManager().RenderUI()
        clear_canvas()

    # 프로그램 종료 시 캔버스를 정리합니다.
    def CleanUp(self) -> None:
        clear_canvas()
        close_canvas()