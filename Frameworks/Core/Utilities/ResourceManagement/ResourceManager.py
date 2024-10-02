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
        if filePath.is_file():
            print(filePath.name)
            return load_image(filePath)  # 파일을 불러오는 함수
        return None  # 파일이 없으면 None 반환

    def LoadSprites(self, _path: str) -> list[Image]:
        dirPath: Path = Path(_path)
        if dirPath.exists() and dirPath.is_dir():
            sprites: list[Image] = []
            for filePath in dirPath.iterdir():
                if (filePath.is_file() and filePath.suffix == ".png"):
                    sprite = self.LoadSprite(filePath)
                    if sprite is not None:
                        sprites.append(sprite)
            return sprites
        return []
