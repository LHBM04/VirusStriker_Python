from abc import ABCMeta, abstractmethod
from ctypes import *
from typing import *

from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *
from pathlib import *

from Core.Objects.Object import Object
from Core.SystemManagement import SystemManager
from Core.Utilities.Singleton import Singleton

class ScriptableObject(Object, metaclass = ABCMeta):
    @abstractmethod
    def ToJson(self):
        ...

    @abstractmethod
    def FromJson(self):
        ...

@final
class Sprite:
    def __init__(self, _texture: SDL_Texture):
        self.__texture: SDL_Texture = _texture

        width: c_int    = c_int(0)
        height: c_int   = c_int(0)

        SDL_QueryTexture(self.__texture, None, None, byref(width), byref(height))

        self.__pivot    = SDL_Point(width.value // 2, height.value // 2)
        self.__rect     = SDL_Rect(0, 0, width.value, height.value)

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    # region Properties
    @property
    def texture(self) -> SDL_Texture:
        return self.__texture

    @property
    def pivot(self) -> SDL_Point:
        return self.__pivot

    @property
    def rect(self) -> SDL_Rect:
        return self.__rect
    # endregion

@final
class Font:
    def __init__(self, _font: TTF_Font) -> None:
        self.__font: TTF_Font = _font

    def __del__(self) -> None:
        ...


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

    def GetTextures(self, _name: str) -> List[SDL_Texture]:
        return self.__textureBank[_name]

    def GetTexture(self, _name: str, _index: int = 0) -> SDL_Texture:
        return self.GetTextures(_name)[_index]