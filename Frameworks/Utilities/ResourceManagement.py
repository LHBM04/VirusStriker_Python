from io import *
from pathlib import Path
from pico2d import *
from Utilities.Singleton import *

class ResourceManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.m_spriteFileBank: dict[str, list[Image]]   = {}
        #self.m_bgmBank: dict[str, mixer.Sound]      = { }   # BGM 뱅크
        #self.m_sfxBank: dict[str, mixer.Sound]      = { }   # SFX 뱅크

    def AddSprite(self, _filePath: str) -> None:
        if str in self.m_spriteFileBank:
            assert(0)
            return
    
        filePaths: list[str] = []
        for filePath in Path(_filePath).iterdir():
            filePaths.append(str(filePath))
        filePaths.sort(key = lambda fileName: int(''.join(filter(str.isdigit, fileName))))  # 숫자 기준으로 정렬

        self.m_spriteFileBank[_filePath] = []
        for filePath in filePaths:
            self.m_spriteFileBank[_filePath].append(load_image(filePath))

    def GetSprite(self, _filePath: str) -> list[Image]:
        if _filePath not in self.m_spriteFileBank.keys():
            self.AddSprite(_filePath)

        return self.m_spriteFileBank[_filePath]