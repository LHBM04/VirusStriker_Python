from argparse import ArgumentError
from typing import final

from pathlib import Path
from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.m_spriteFileBank: dict[str, list[Image]]   = {}
        #self.m_bgmBank: dict[str, mixer.Sound]      = { }   # BGM 뱅크
        #self.m_sfxBank: dict[str, mixer.Sound]      = { }   # SFX 뱅크

    def AddSprite(self, filePath: str) -> None:
        if filePath in self.m_spriteFileBank:
            raise ValueError(f"File path {filePath} is already registered.")

            # 파일 경로 목록을 수집하여 숫자 기준으로 정렬
        filePaths: list[str] = sorted(
            [str(filePath) for filePath in Path(filePath).iterdir()],
            key=lambda fileName: int(''.join(filter(str.isdigit, Path(fileName).stem)) or 0)
        )

        # 이미지를 로드하여 m_spriteFileBank에 저장
        self.m_spriteFileBank[filePath] = [load_image(filePath) for filePath in filePaths]

    def GetSprite(self, _filePath: str) -> list[Image]:
        if _filePath not in self.m_spriteFileBank.keys():
            self.AddSprite(_filePath)

        return self.m_spriteFileBank[_filePath]