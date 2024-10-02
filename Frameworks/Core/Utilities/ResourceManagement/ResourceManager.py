import os.path
from argparse import ArgumentError
from typing import final
from pathlib import Path

from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass = Singleton):
    def __init__(self):
        self.imageBank: dict[str : list[Image]]   = {}
        self.bgmBank: dict[str : Wav]       = {}
        self.sfxBank: dict[str: Wav]        = {}

    def InitializeResource(self) -> None:
        yield self.LoadAllImage("Resources\\Sprites")
        yield self.LoadAllAudio("Resources\\Audio\\BGM")
        yield self.LoadAllAudio("Resources\\Audio\\BGM")
        yield None

    def LoadImage(self, _filePath: str) -> (str, Image):
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise ArgumentError(f"[Oops!] 파일 경로가 잘못 되었습니다. 경로는 \"{str(filePath)}\"였습니다.")

        yield load_image(filePath)

    def LoadAllImage(self, _directoryPath: str) -> list[Image]:
        directoryPath: Path = Path(_directoryPath)
        if not directoryPath.exists() or not directoryPath.is_dir():
            raise ArgumentError(f"[Oops!] 폴더 경로가 잘못 되었습니다. \"{str(directoryPath)}\"였습니다.")

        self.imageBank[str(directoryPath)] = []
        for filePath in directoryPath.iterdir():
            self.imageBank[str(filePath)].append(self.LoadImage(filePath))

    def GetImage(self, _key: str) -> Image:
        if _key not in self.imageBank:
            raise KeyError(f"[Oops!] 키값이 잘못 되었습니다. 키는 \"{str(_key)}\"였습니다.")

        return self.imageBank[_key]

    def LoadAudio(self, _filePath: str) -> Wav:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise ArgumentError(f"[Oops!] 파일 경로가 잘못 되었습니다. 경로는 \"{str(filePath)}\"였습니다.")

        yield load_wav(filePath)

    def LoadAllAudio(self, _directoryPath: str) -> list[Wav]:
        directoryPath: Path = Path(_directoryPath)
        if not directoryPath.exists() or not directoryPath.is_dir():
            raise ArgumentError(f"[Oops!] 폴더 경로가 잘못 되었습니다. \"{str(directoryPath)}\"였습니다.")

        audioBank: list[Wav] = []
        for filePath in directoryPath.iterdir():
            audioBank[str(filePath)] = self.LoadAudio(filePath)

        yield audioBank

    def GetBGM(self, _key) -> Wav:
        if _key not in self.bgmBank:
            raise KeyError(f"[Oops!] 키값이 잘못 되었습니다. 키는 \"{_key}\"였습니다.")

        return self.bgmBank[_key]

    def GetSFX(self, _key: str) -> Wav:
        if _key not in self.sfxBank:
            raise KeyError(f"[Oops!] 키값이 잘못 되었습니다. 키는 \"{_key}\"였습니다.")

        return self.sfxBank[_key]