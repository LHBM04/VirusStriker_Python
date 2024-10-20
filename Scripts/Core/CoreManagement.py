import time
from ctypes import *
from json import *
from typing import *

from sdl2 import *
from pathlib import *

from Core.Utilities.InputManagement import InputManager
from Core.Utilities.Singleton import Singleton
from Level.SceneManagement import SceneManager

@final
class Core(metaclass = Singleton):
    def __init__(self):
        # region Const Field
        self.__DEFAULT_WINDOW_WIDTH: int    = 1280
        self.__DEFAULT_WINDOW_HEIGHT: int   = 720
        self.__DEFAULT_WINDOW_STATE: int    = SDL_WINDOW_SHOWN
        self.__DEFAULT_WINDOW_SYNC: int     = SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
        # endregion

        self.__windowHandle: Optional[SDL_Window]       = None
        self.__rendererHandle: Optional[SDL_Renderer]   = None

        self.__isRunning: bool      = False
        self.__windowWidth: int     = self.__DEFAULT_WINDOW_WIDTH
        self.__windowHeight: int    = self.__DEFAULT_WINDOW_HEIGHT
        self.__screenState: int     = self.__DEFAULT_WINDOW_STATE
        self.__syncState: int       = self.__DEFAULT_WINDOW_SYNC

    @property
    def windowHandle(self) -> SDL_Window:
        return self.__windowHandle

    @property
    def windowWidth(self) -> int:
        return self.__windowWidth

    @property
    def windowHeight(self) -> int:
        return self.__windowHeight

    def Initialize(self) -> None:
        settingFile: Path = Path(r"Resources\Setting\Setting.json")
        if not settingFile.exists() or not settingFile.is_file():
            self.__windowWidth     = self.__DEFAULT_WINDOW_WIDTH
            self.__windowHeight    = self.__DEFAULT_WINDOW_HEIGHT
            self.__screenState     = self.__DEFAULT_WINDOW_STATE
            self.__syncState       = self.__DEFAULT_WINDOW_SYNC

        else:
            with settingFile.open('r') as file:
                settingData: Dict[str, bytes] = load(file)

                self.__windowWidth  = settingData.get("Window Width")
                self.__windowHeight = settingData.get('Window Height')
                self.__screenState  = settingData.get('Fullscreen')
                self.__syncState    = settingData.get('Sync')

        SDL_Init(SDL_INIT_EVERYTHING)
        self.__windowHandle = SDL_CreateWindow(
            f"Virus Striker {self.__windowWidth} x {self.__windowHeight}".encode('utf-8'),
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED,
            self.__windowWidth,
            self.__windowHeight,
            self.__screenState)

        self.__rendererHandle = SDL_CreateRenderer(
            self.__windowHandle,
            -1,
            self.__syncState
        )

    def Run(self) -> None:
        self.__isRunning = True

        previousTime: float     = time.time()
        fixedUpdateTime: float  = 1.0 / 50.0
        fixedDeltaTime: float   = 0.0

        while self.__isRunning:
            self.ProceedEvent()

            SDL_SetRenderDrawColor(self.__rendererHandle, 0, 0, 0, 255)
            SDL_RenderClear(self.__rendererHandle)

            if SceneManager().isResetDeltaTime:
                previousTime = time.time()

            currentTime: float  = time.time()
            deltaTime:float     = currentTime - previousTime

            previousTime = currentTime

            fixedDeltaTime += deltaTime
            if fixedDeltaTime >= 2.0:
                fixedDeltaTime = 2.0

            while fixedDeltaTime > fixedUpdateTime:
                fixedDeltaTime -= fixedUpdateTime
                SceneManager().FixedUpdate(fixedUpdateTime)

            InputManager().Update()
            SceneManager().Update(deltaTime)
            SceneManager().Render()

            SDL_RenderPresent(self.__rendererHandle)

        SDL_DestroyRenderer(self.__rendererHandle)
        SDL_DestroyWindow(self.__windowHandle)
        SDL_Quit()

    def ProceedEvent(self) -> SDL_Event:
        event: SDL_Event = SDL_Event()
        while SDL_PollEvent(byref(event)):
            if event.type == SDL_QUIT:
                self.__isRunning = False

            elif event.type in { SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP }:
                InputManager().ProceedInput(event)

        return event

    def ResizeWindow(self) -> None:
        pass
