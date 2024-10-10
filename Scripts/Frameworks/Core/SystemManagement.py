from typing import final

from pico2d import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.InputManagement import InputManager
from Level.SceneManagement import SceneManager


@final
class SystemManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.__isRunning: bool      = True              # 프로그램 구동 여부.

        self.__windowName: str      = "Virus Striker"   # 프로그램(윈도우) 이름.
        self.__windowWidth: int     = 1280              # 가로 해상도 (테스트).
        self.__windowHeight: int    = 720               # 세로 해상도 (테스트).

        self.__gameFPS: float       = 0.0               # 게임 초당 프레임.
        self.__fpsDeltaTime: float  = 0.0
        self.__maxFpsRate: float    = 60

    @property
    def windowName(self) -> str:
        return self.__windowName

    @property
    def windowWidth(self):
        return self.__windowWidth

    @property
    def windowHeight(self):
        return self.__windowHeight

    @property
    def isRunning(self) -> bool:
        return self.__isRunning

    @property
    def fps(self) -> float:
        return self.__gameFPS

    @fps.setter
    def fps(self, _rate) -> None:
        self.__gameFPS = _rate

    def Update(self, _deltaTime: float) -> None:
        from Level.SceneManagement import SceneManager
        SceneManager().Update(_deltaTime)
        InputManager().Update()
        #AudioManager().Update()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        from Level.SceneManagement import SceneManager
        SceneManager().FixedUpdate(_fixedDeltaTime)

    def Render(self):
        clear_canvas()
        SceneManager().Render()
        SceneManager().RenderDebug()
        update_canvas()

    # 프로그램 종료 시 캔버스를 정리합니다.
    def CleanUp(self) -> None:
        clear_canvas()
        close_canvas()

    def Quit(self):
        self.__isRunning = False