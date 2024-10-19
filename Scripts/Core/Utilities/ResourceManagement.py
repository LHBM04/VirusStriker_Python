from abc import ABCMeta, abstractmethod
from importlib.abc import ResourceLoader
from typing import Any, final, Dict, Optional, Sequence, List, Tuple, Generator, Iterable, Iterator

from pathlib import *
from pico2d import *

from Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass = Singleton):
    """
    게임 내 사용되는 리소스를 일기 및 저장합니다.
    """
    def __init__(self):
        self.__spriteBank: Dict[str, List[Image]]   = {}    # 읽어온 Sprite를 이곳에 경로와 함께 저장합니다.
        self.__spriteResourcePath: Path             = Path(r"Resources\Sprites")
        self.__spriteResourceSuffix: str            = "*.png"

        self.__bgmBank: Dict[str, Music]    = {}    # 읽어온 BGM을 이곳에 경로와 함께 저장합니다.
        self.__bgmResourcePath: Path        = Path(r"Resources\Audio\BGM")
        self.__sfxBank: Dict[str, Music]    = {}    # 읽어온 SFX를 이곳에 경로와 함께 저장합니다.
        self.__sfxResourcePath: Path        = Path(r"Resources\Audio\SFX")
        self.__audioResourceSuffix: str     = "*.flac"

        self.__fontBank: Dict[str, Font]    = {}    # 읽어온 Font를 이곳에 경로와 함께 저장합니다.
        self.__fontResourcePath: Path       = Path(r"Resources\Fonts")
        self.__fontResourceSuffix: str      = "*.otf"

    def Initialize(self) -> None:
        self.LoadImages()
        self.LoadBGM()
        self.LoadSFX()
        self.LoadFont()

    def LoadImages(self) -> None:
        if not self.__spriteResourcePath.exists() or not self.__spriteResourcePath.is_dir():
            pass

        for filePath in self.__spriteResourcePath.rglob(self.__spriteResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            if filePath.name not in self.__spriteBank:
                self.__spriteBank[filePath.name] = []

            print(str(filePath))
            self.__spriteBank[filePath.name].append(load_image(str(filePath)))

    def LoadBGM(self) -> None:
        if not self.__bgmResourcePath.exists() or not self.__bgmResourcePath.is_dir():
            raise IOError

        for filePath in self.__bgmResourcePath.rglob(self.__audioResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__bgmBank[filePath.name] = load_music(str(filePath))

    def LoadSFX(self) -> None:
        if not self.__sfxResourcePath.exists() or not self.__sfxResourcePath.is_dir():
            raise IOError

        for filePath in self.__sfxResourcePath.rglob(self.__audioResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__sfxBank[filePath.name] = load_music(str(filePath))

    def LoadFont(self) -> None:
        if not self.__fontResourcePath.exists() or not self.__fontResourcePath.is_dir():
            raise IOError

        for filePath in self.__fontResourcePath.rglob(self.__fontResourceSuffix):
            if not filePath.exists() or not filePath.is_file():
                raise IOError

            print(str(filePath))
            self.__fontBank[filePath.name] = load_font(str(filePath), 20)