from numpy import *
from typing import *

from multipledispatch import dispatch
from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *
from pathlib import *

from Core.SystemManagement import SystemManager
from Core.Utilities.Singleton import Singleton

@final
class Sprite:
    def __init__(self, _texture: SDL_Texture):
        self.__texture: SDL_Texture     = _texture
        self.__width: int               = 0
        self.__height: int              = 0

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    def __InitSDLRect(self, _x: int, _y: int, _w: int, _h: int) -> SDL_Rect:
        return SDL_Rect(int(_x), int(-_y + SystemManager().windowHeight - _h), int(_w), int(_h))

    @dispatch(int, int)
    def Draw(self, _x: int, _y: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - self.__width) // 2, (_y - self.__height) // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, 0.0, None, SDL_FLIP_NONE)

    @dispatch(int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - self.__width) // 2, (_y - self.__height) // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, SDL_FLIP_NONE)

    @dispatch(int, int, int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int, _width: int, _height: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, SDL_FLIP_NONE)

    @dispatch(int, int, int, int, int, bool, bool)
    def Draw(self, _x: int, _y: int, _rotate: int, _width: int, _height: int, _flipX: bool, _flipY: bool) -> None:
        rect: SDL_Rect  = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        flipFlag: int   = ((SDL_FLIP_VERTICAL if _flipX else SDL_FLIP_NONE) | (SDL_FLIP_HORIZONTAL if _flipY else SDL_FLIP_NONE))

        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, flipFlag)

@final
class ResourceManager(metaclass = Singleton):
    # TODO: 멀티 스레딩으로 리소스 긁어오는 거 고려해보자.
    def __init__(self):
        self.__textureBank: Dict[str, List[SDL_Texture]]    = { }
        self.__bgmBank: Dict[str, Mix_Music]                = { }
        self.__sfxBank: Dict[str, Mix_Music]                = { }
        self.__ttfBank: Dict[str, TTF_Font]                 = { }

        self.__textureResourcePath: Path    = Path(r"Resources\Sprites")
        self.__textureResourceSuffix: str   = "*.png"

        self.__bgmResourcePath: Path    = Path(r"Resources\Audio\BGM")
        self.__sfxResourcePath: Path    = Path(r"Resources\Audio\SFX")
        self.__audioResourceSuffix: str = "*.flac"

        self.__fontResourcePath: Path   = Path(r"Resources\Fonts")
        self.__fontResourceSuffix: str  = "*.otf"

        IMG_Init(IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | IMG_INIT_WEBP)
        TTF_Init()

    def __del__(self):
        TTF_Quit()
        IMG_Quit()

    def Initialize(self) -> None:
        self.LoadTextures()
        self.LoadBGM()
        self.LoadSFX()
        self.LoadFont()

    def LoadTextures(self) -> None:
        if not self.__textureResourcePath.exists() or not self.__textureResourcePath.is_dir():
            pass

        for filePath in self.__textureResourcePath.rglob(self.__textureResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            if filePath.name not in self.__textureBank:
                self.__textureBank[filePath.name] = []

            print(str(filePath))
            self.__textureBank[filePath.name].append(IMG_LoadTexture(SystemManager().rendererHandle, str(filePath).encode("UTF-8")))

    def LoadBGM(self) -> None:
        if not self.__bgmResourcePath.exists() or not self.__bgmResourcePath.is_dir():
            raise IOError

        for filePath in self.__bgmResourcePath.rglob(self.__audioResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__bgmBank[filePath.name] = Mix_LoadMUS(str(filePath).encode("UTF-8"))

    def LoadSFX(self) -> None:
        if not self.__sfxResourcePath.exists() or not self.__sfxResourcePath.is_dir():
            raise IOError

        for filePath in self.__sfxResourcePath.rglob(self.__audioResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__sfxBank[filePath.name] = Mix_LoadMUS(str(filePath).encode("UTF-8"))

    def LoadFont(self) -> None:
        if not self.__fontResourcePath.exists() or not self.__fontResourcePath.is_dir():
            raise IOError

        for filePath in self.__fontResourcePath.rglob(self.__fontResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            # TODO: Font 파일 읽어오기
            # self.__fontBank[filePath.name] = load_font(str(filePath), 20)
