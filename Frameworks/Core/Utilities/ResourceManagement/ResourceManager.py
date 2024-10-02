from argparse import ArgumentError
from typing import final
from pathlib import Path

from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.m_spriteFileBank: dict[str, list[Image]]   = {}

    def GetSprite(self, _path: str, _index: int = 0) -> Image:
        if _path not in self.m_spriteFileBank.keys():
            self.m_spriteFileBank[_path] = self.LoadSprites(_path)

        return self.m_spriteFileBank[_path][_index]

    def GetSprites(self, _path: str) -> list[Image]:
        if _path not in self.m_spriteFileBank.keys():
            self.m_spriteFileBank[_path] = self.LoadSprites(_path)

        return self.m_spriteFileBank[_path]

    def LoadSprite(self, _path: str) -> Image:
        filePath: Path = Path(_path)
        print(Path)
        if not filePath.exists() or not filePath.is_file():
            raise ValueError

        return load_image(filePath)

    def LoadSprites(self, _path: str) -> list[Image]:
        for root, _, files in os.walk(_path):
            for file in files:
                if not file.endswith(".png"):
                    continue
                file_path = os.path.join(root, file)
                yield file_path, file

    def Temp(self, _path: str) -> list[Image]:
        for root, _, files in os.walk(_path):
            for file in files:
                if not file.endswith(".png"):
                    continue
                file_path = os.path.join(root, file)
                yield file_path, file
