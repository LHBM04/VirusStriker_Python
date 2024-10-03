from typing import final

from pathlib import Path
from pico2d import *

from Core.Utilities.Singleton import Singleton


def LoadAll(_directoryPath: str, _suffix: str, _callback: callable) -> str:
    directory = Path(_directoryPath)
    if not (directory.exists() and directory.is_dir()):
        raise IOError

    for filePath in directory.iterdir():
        if not (filePath.exists() and filePath.is_file()):
            raise IOError
        elif filePath.suffix is not _suffix:
            continue

        callable(filePath)
        yield str(filePath)

@final
class ResourceManager(metaclass = Singleton):
    def __init__(self):
        self.imageBank: dict[str : Image]   = {}
        self.bgmBank: dict[str : Wav]       = {}
        self.sfxBank: dict[str: Wav]        = {}

    def AddImage(self, _filePath) -> None:
        self.imageBank[_filePath] = load_image(_filePath)

    def AddBGM(self, _filePath) -> None:
        self.bgmBank[_filePath] = load_music(_filePath)

    def AddSFX(self, _filePath) -> None:
        self.sfxBank[_filePath] = load_wav(_filePath)

    def LoadImage(self) -> (str, str):
        return LoadAll(r"Resources\Sprites", '.png', self.AddImage)

    def LoadBGM(self) -> (str, str):
        return LoadAll(r"Resources\Audio\BGM", '.wav', self.AddBGM)

    def LoadSFX(self) -> (str, str):
        return LoadAll(r"Resources\Audio\SFX", '.wav', self.AddSFX)

    def GetImage(self, _filePath) -> Image:
        return self.imageBank[_filePath]

    def GetBGM(self, _filePath) -> Music:
        return self.bgmBank[_filePath]

    def GetSFX(self, _filePath: str) -> Wav:
        return self.sfxBank[_filePath]