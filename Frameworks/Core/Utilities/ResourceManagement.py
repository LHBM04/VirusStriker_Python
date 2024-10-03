from typing import final

import re
from pathlib import Path
from pico2d import *

from Core.Utilities.Singleton import Singleton

def LoadAll(_directoryPath: str, _suffix: str, _callback: callable) -> None:
    directoryPath = Path(_directoryPath)
    if not directoryPath.exists() or not directoryPath.is_dir():
        raise IOError(f"'{_directoryPath}'는 유효한 디렉토리가 아닙니다.")

    for filePath in sorted(directoryPath.rglob('*'),
                           key = lambda p: [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', Path(p).name)]):
        if filePath.is_file() and filePath.suffix == _suffix:
            yield _callback(str(filePath))

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

    def LoadImage(self) -> str:
        return LoadAll(r"Resources\Sprites", '.png', self.AddImage)

    def LoadBGM(self) -> str:
        return LoadAll(r"Resources\Audio\BGM", '.wav', self.AddBGM)

    def LoadSFX(self) -> str:
        return LoadAll(r"Resources\Audio\SFX", '.wav', self.AddSFX)

    def GetImage(self, _filePath) -> Image:
        return self.imageBank[_filePath]

    def GetBGM(self, _filePath) -> Music:
        return self.bgmBank[_filePath]

    def GetSFX(self, _filePath: str) -> Wav:
        return self.sfxBank[_filePath]