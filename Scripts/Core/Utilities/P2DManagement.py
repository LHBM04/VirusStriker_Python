from typing import final
from time import time as GetTime

from pico2d import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.InputManagement import InputManager
from Level.SceneManagement import SceneManager

@final
class P2DManager(metaclass = Singleton):
    def __init__(self):
        self.__isGameRunning: bool  = True              # 프로그램 구동 여부.
        self.__windowTitle: str     = "Virus Striker"   # 윈도우 창 타이틀.

        self.__windowWidth: int     = 1280              # 윈도우 창 폭.
        self.__windowHeight: int    = 720               # 윈도우 창 높이.
        self.__isFullScreen: bool   = False             # 전체 화면 여부.
        self.__isSync: bool         = True              # 수직 동기화 여부.

    @property
    def isGameRunning(self) -> bool:
        """
        해당 게임의 구동 여부를 반환합니다.
        :return: 해당 게임의 구동 여부.
        """
        return self.__isGameRunning

    @property
    def windowTitle(self) -> str:
        """
        윈도우 창의 타이틀 이름을 반환합니다.
        :return: 윈도우 창의 상단 이름.
        """
        return self.__windowTitle

    @property
    def windowWidth(self) -> int:
        """
        윈도우 창의 폭을 반환합니다.
        :return: 윈도우 창의 폭.
        """
        return self.__windowWidth

    @property
    def windowHeight(self) -> int:
        """
        윈도우 창의 높이를 반환합니다.
        :return: 윈도우 창의 높이.
        """
        return self.__windowHeight

    @property
    def isFullScreen(self) -> bool:
        """
        윈도우 창의 풀 스크린 여부를 반환합니다.
        :return:
        """
        return self.__isFullScreen

    @property
    def isSync(self) -> bool:
        """
        윈도우 창의 수직 동기화 여부를 반환합니다.
        :return: 윈도우 창의 수직 동기화 여부.
        """
        return self.__isSync

    def Initialize(self) -> None:
        open_canvas(
            self.__windowWidth,
            self.__windowHeight,
            self.__isSync,
            self.__isFullScreen)
        SDL_SetWindowTitle(
            pico2d.window,
            self.__windowTitle.encode('utf-8'))

    def Run(self) -> None:
        self.__isGameRunning = True

        previousTime: float = GetTime()

        fixedUpdateTime: float = 1.0 / 50.0
        fixedDeltaTime: float = 0.0

        while self.__isGameRunning:
            self.ProceedMessage()
            clear_canvas()

            if SceneManager().isResetDeltaTime:
                previousTime = GetTime()

            currentTime: float  = GetTime()
            deltaTime:float     = currentTime - previousTime

            previousTime = currentTime

            fixedDeltaTime += deltaTime
            if fixedDeltaTime >= 2.0:
                fixedDeltaTime = 2.0

            while fixedDeltaTime > fixedUpdateTime:
                fixedDeltaTime -= fixedUpdateTime
                SceneManager().FixedUpdate(fixedDeltaTime)

            InputManager().Update()
            SceneManager().Update(deltaTime)
            SceneManager().Render()
            update_canvas()

        clear_canvas()
        close_canvas()

    def ProceedMessage(self) -> None:
        gotEvent: SDL_Event = SDL_Event()
        while SDL_PollEvent(ctypes.byref(gotEvent)):
            event: Event = Event(gotEvent.type)
            if event.type == SDL_QUIT:
                self.__isGameRunning = False

            elif event.type in { SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP }:
                if event.type in { SDL_KEYDOWN, SDL_KEYUP } and not gotEvent.key.repeat:
                    event.key = gotEvent.key.keysym.sym

                elif event.type in { SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP } or event.type == SDL_MOUSEMOTION:
                    event.button, event.x, event.y = gotEvent.button.button, gotEvent.button.x, gotEvent.button.y

                InputManager().ProceedInput(event)
            else:
                pass
