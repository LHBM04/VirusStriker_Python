from abc import ABCMeta, abstractmethod
from typing import *

from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *
from pathlib import *

from Core.SystemManagement import SystemManager
from Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass = Singleton):
    # TODO: 멀티 스레딩으로 리소스 긁어오는 거 고려해보자.
    def __init__(self):
        self.__textureBank: Dict[str, List[SDL_Texture]]    = { }
        self.__bgmBank: Dict[str, Mix_Chunk]                = { }
        self.__sfxBank: Dict[str, Mix_Chunk]                = { }
        self.__ttfBank: Dict[str, TTF_Font]                 = { }

        self.__textureResourcePath: Path    = Path(r"Resources\Sprites")
        self.__textureResourceSuffix: str   = "*.png"

        self.__bgmResourcePath: Path    = Path(r"Resources\Audio\BGM")
        self.__sfxResourcePath: Path    = Path(r"Resources\Audio\SFX")
        self.__audioResourceSuffix: str = "*.flac"

        self.__fontBank: Dict[str, TTF_Font]    = {}
        self.__fontResourcePath: Path           = Path(r"Resources\Fonts")
        self.__fontResourceSuffix: str          = "*.otf"

        IMG_Init(IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | IMG_INIT_WEBP)
        TTF_Init()

    def __del__(self):
        TTF_Quit()
        IMG_Quit()

    def Initialize(self) -> None:
        # Initialize SDL audio
        if SDL_Init(SDL_INIT_AUDIO) != 0:
            print(f"Failed to initialize SDL audio: {SDL_GetError()}")
            return

        Mix_Init(MIX_INIT_MP3 | MIX_INIT_OGG | MIX_INIT_FLAC)

        # Open the audio device
        if Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, MIX_DEFAULT_CHANNELS, 1024) < 0:
            print(f"Failed to initialize audio: {Mix_GetError()}")
            return

        # Set number of channels (should be after Mix_OpenAudio)
        if Mix_AllocateChannels(MIX_CHANNELS) == 0:
            print(f"Failed to allocate channels: {Mix_GetError()}")

        # self.LoadTextures()
        self.LoadBGM()
        self.LoadSFX()
        #self.LoadFont()

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
            self.__bgmBank[filePath.name] = Mix_LoadWAV(str(filePath).encode("UTF-8"))

    def LoadSFX(self) -> None:
        if not self.__sfxResourcePath.exists() or not self.__sfxResourcePath.is_dir():
            raise IOError

        for filePath in self.__sfxResourcePath.rglob(self.__audioResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__sfxBank[filePath.name] = Mix_LoadWAV(str(filePath).encode("UTF-8"))

    def LoadFont(self) -> None:
        if not self.__fontResourcePath.exists() or not self.__fontResourcePath.is_dir():
            raise IOError

        for filePath in self.__fontResourcePath.rglob(self.__fontResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__fontBank[filePath.name] = TTF_OpenFont(str(filePath).encode('utf-8'), 20)

    def GetTextures(self, _name: str) -> List[SDL_Texture]:
        return self.__textureBank[_name]

    def GetTexture(self, _name: str, _index: int = 0) -> SDL_Texture:
        return self.GetTextures(_name)[_index]

    def GetFont(self, _name: str, _size: int = 25) -> TTF_Font:
        return self.__fontBank[_name]

    def GetBGM(self, _name: str) -> Mix_Chunk:
        return self.__bgmBank[_name]