from pathlib import Path
from pico2d import *
from pygame import mixer
from Utilities.Singleton import *

class FileManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.textureBank: dict[str, list[Image]] = { }
        self.bgmBank: dict[str, mixer.Sound] = { }
        self.sfxBank: dict[str, mixer.Sound] = { }

    def AddSprite(self, _filePath: str) -> None:
        if str in self.textureBank:
            assert(0)
            return
    
        filePaths: list[str] = []
        for filePath in Path(_filePath).iterdir():
            filePaths.append(str(filePath))
        filePaths.sort(key = lambda fileName: int(''.join(filter(str.isdigit, fileName))))  # 숫자 기준으로 정렬

        self.textureBank[_filePath] = []
        for filePath in filePaths:
            self.textureBank[_filePath].append(load_image(filePath))

    def GetSprite(self, _filePath: str) -> list[Image]:
        if _filePath not in self.textureBank.keys():
            self.AddSprite(_filePath)

        return self.textureBank[_filePath]
