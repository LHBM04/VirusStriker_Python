import os.path
from typing import final

from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton

def LoadAll(_directoryPath: str, _suffix: str, _callback: callable) -> (str, str):
    for root, _, files in os.walk(_directoryPath):
        for file in files:
            if not file.endswith(_suffix):
                continue
            filePath = os.path.join(root, file)
            _callback(filePath)
            yield filePath, file

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
        return LoadAll("Resources\\Sprites", '.png', self.AddImage)

    def LoadBGM(self) -> (str, str):
        return LoadAll("Resources\\Audio\\BGM", '.wav', self.AddBGM)

    def LoadSFX(self) -> (str, str):
        return LoadAll("Resources\\Audio\\SFX", '.wav', self.AddSFX)

    def GetImage(self, _filePath) -> Image:
        return self.imageBank[_filePath]

    def GetBGM(self, _filePath) -> Music:
        return self.bgmBank[_filePath]

    def GetSFX(self, _filePath: str) -> Wav:
        return self.sfxBank[_filePath]