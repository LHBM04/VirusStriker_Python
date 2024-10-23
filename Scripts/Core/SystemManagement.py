from ctypes import *
from json import *
from typing import *

from sdl2 import *
from pathlib import *

from Core.Utilities.InputManagement import InputManager
from Core.Utilities.Singleton import Singleton
from Level.SceneManagement import SceneManager

@final
class SystemManager(metaclass = Singleton):
    def __init__(self):
        # region Const Field
        self.__GAME_TITLE: str              = "Virus Striker"
        self.__GAME_VERSION: str            = "Alpha 1.0"

        self.__DEFAULT_WINDOW_WIDTH: int    = 1280
        self.__DEFAULT_WINDOW_HEIGHT: int   = 720
        self.__DEFAULT_WINDOW_STATE: int    = SDL_WINDOW_SHOWN | SDL_WINDOW_OPENGL
        self.__DEFAULT_WINDOW_SYNC: int     = SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
        # endregion

        self.__windowHandle: Optional[SDL_Window]       = None
        self.__rendererHandle: Optional[SDL_Renderer]   = None

        self.__isRunning: bool      = False
        self.__windowWidth: int     = self.__DEFAULT_WINDOW_WIDTH
        self.__windowHeight: int    = self.__DEFAULT_WINDOW_HEIGHT
        self.__screenState: int     = self.__DEFAULT_WINDOW_STATE
        self.__syncState: int       = self.__DEFAULT_WINDOW_SYNC

        SDL_Init(SDL_INIT_EVERYTHING)

    def __del__(self):
        SDL_DestroyRenderer(self.__rendererHandle)
        SDL_DestroyWindow(self.__windowHandle)
        SDL_Quit()

    @property
    def windowHandle(self) -> SDL_Window:
        if self.__windowHandle is None:
            raise ValueError()

        return self.__windowHandle

    @property
    def windowWidth(self) -> int:
        return self.__windowWidth

    @property
    def windowHeight(self) -> int:
        return self.__windowHeight

    @property
    def rendererHandle(self) -> SDL_Renderer:
        if self.__rendererHandle is None:
            raise ValueError()

        return self.__rendererHandle

    def Initialize(self) -> None:
        print("[Notice] Configuration.json을 찾고 있습니다.")
        settingFile: Path = Path(r"Resources\Configuration.json")

        if not settingFile.exists() or not settingFile.is_file():
            print("[Caution!] Configuration.json을 찾지 못했습니다. 기본 설정으로 기동합니다...")
            self.__windowWidth     = self.__DEFAULT_WINDOW_WIDTH
            self.__windowHeight    = self.__DEFAULT_WINDOW_HEIGHT
            self.__screenState     = self.__DEFAULT_WINDOW_STATE
            self.__syncState       = self.__DEFAULT_WINDOW_SYNC

        else:
            with settingFile.open('r') as file:
                settingData: Dict[str, bytes] = load(file)

                print("[Notice] Setting.json을 찾았습니다. 해당 설정으로 기동합니다.")
                self.__windowWidth  = settingData.get("Window Width")
                self.__windowHeight = settingData.get('Window Height')
                self.__screenState  = settingData.get('Screen State')
                self.__syncState    = settingData.get('Sync State')

        print("[Notice] Window를 생성합니다.")
        self.__windowHandle = SDL_CreateWindow(
            f"{self.__GAME_TITLE} Ver. {self.__GAME_VERSION} ({self.__windowWidth} x {self.__windowHeight})".encode('utf-8'),
            SDL_WINDOWPOS_CENTERED,
            SDL_WINDOWPOS_CENTERED,
            self.__windowWidth,
            self.__windowHeight,
            self.__screenState)

        if self.__windowHandle is None:
            raise ValueError("[Oops!] Window 핸들 생성에 실패했습니다!")

        print("[Notice] Renderer를 생성합니다.")
        self.__rendererHandle = SDL_CreateRenderer(
            self.__windowHandle,
            -1,
            self.__syncState
        )

        # Fallback
        if self.__rendererHandle is None:
            print("[Caution!] Renderer 핸들 생성에 실패했습니다. 기본 설정으로 재생성합니다...")
            self.__rendererHandle = SDL_CreateRenderer(self.__windowHandle, -1, SDL_RENDERER_SOFTWARE)

            if self.__rendererHandle is None:
                raise ValueError("[Oops!] Renderer 핸들 생성에 실패했습니다!")

        from Core.Utilities.ResourceManagement import ResourceManager
        ResourceManager().Initialize()

    def Run(self) -> None:
        print("[Notice] 프로그램을 기동합니다.")
        self.__isRunning = True

        previousTime: int       = SDL_GetTicks()
        fixedUpdateTime: float  = 1.0 / 50.0
        fixedDeltaTime: float   = 0.0

        from Core.Utilities.ResourceManagement import ResourceManager

        def __InitSDLRect(_x: int, _y: int, _w: int, _h: int) -> SDL_Rect:
            return SDL_Rect(int(_x), int(-_y + SystemManager().windowHeight - _h), int(_w), int(_h))

        testTexture: SDL_Texture = ResourceManager().GetTexture("Sprite_Background_Initialize.png")
        width: c_int = c_int(0)
        height: c_int = c_int(0)
        SDL_QueryTexture(testTexture, None, None, byref(width), byref(height))

        while self.__isRunning:
            self.ProceedEvent()

            SDL_RenderClear(self.__rendererHandle)

            rectangle: SDL_Rect = __InitSDLRect(0 - width.value // 2, 0 - height.value // 2, width.value, height.value)
            SDL_RenderCopyEx(self.__rendererHandle, testTexture, None, rectangle, 0.0, None, 0)

            if SceneManager().isResetDeltaTime:
                previousTime = SDL_GetTicks()

            currentTime: int    = SDL_GetTicks()
            deltaTime: float    = (currentTime - previousTime) / 1000.0

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

    def Quit(self) -> None:
        self.__isRunning = False

    def ProceedEvent(self) -> SDL_Event:
        event: SDL_Event = SDL_Event()
        while SDL_PollEvent(byref(event)):
            if event.type == SDL_QUIT:
                self.__isRunning = False

            elif event.type in { SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP }:
                InputManager().ProceedInput(event)

        return event

    def ResizeWindow(self, _width: int, _height: int) -> None:
        self.__windowWidth  = _width
        self.__windowHeight = _height

        SDL_SetWindowSize(self.__windowWidth, self.__windowWidth)
        SDL_SetWindowTitle(f"{self.__GAME_TITLE} Ver. {self.__GAME_VERSION} ({self.__windowWidth} x {self.__windowHeight})".encode('utf-8'))

        SDL_RenderClear(self.__rendererHandle)
        SDL_RenderPresent(self.__rendererHandle)
