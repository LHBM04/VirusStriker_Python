from typing import final

from pico2d import *

from Frameworks.Core.Utilities.ResourceManagement.ResourceManager import ResourceManager
from Frameworks.Core.Utilities.Singleton import Singleton
from Frameworks.Core.Utilities.InputManagement.InputManager import InputManager
from Frameworks.Level.SceneManager import SceneManager
from Frameworks.Level.Stages.OpeningScene import OpeningScene
from Frameworks.Level.Stages.TitleScene import TitleScene


@final
class SystemManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.windowName: str    = "Virus Striker"   # 프로그램(윈도우) 이름.
        self.windowWidth: int   = 1280              # 가로 해상도 (테스트).
        self.windowHeight: int  = 800               # 세로 해상도 (테스트).
        self.isRunning: bool    = True              # 프로그램 구동 여부.
        self.gameFPS: float     = 0.0               # 게임 초당 프레임.
        self.fpsRate            = 60

    def Inintialize(self) -> None:
        open_canvas(self.windowWidth, self.windowHeight, False, False) # 캔버스 열기
        SDL_SetWindowTitle(pico2d.window, self.windowName.encode('utf-8'))      # 윈도우 이름 변경

        displayMode                = SDL_DisplayMode()
        displayMode.format         = SDL_PIXELFORMAT_RGBA8888  # 픽셀 포맷
        displayMode.w              = self.windowWidth  # 너비
        displayMode.h              = self.windowHeight  # 높이
        displayMode.refresh_rate   = self.fpsRate  # 리프레시 레이트

        initBackground: Image = load_image("Resources\\Sprites\\Backgrounds\\Sprite_Background_Initialize.png")
        initBackground.draw(get_canvas_width() / 2,
                            get_canvas_height() / 2,
                            get_canvas_width(),
                            get_canvas_height())

        update_canvas()

        yield ResourceManager().InitializeResource()

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