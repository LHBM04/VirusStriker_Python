from pathlib import Path
from typing import Dict, Sequence, List, final

from pico2d import *

from Core.Utilities.Singleton import Singleton

# 게임 내 사용될 리소스를 불러온 뒤, 저장합니다.
@final
class ResourceLoader(metaclass=Singleton):
    def __init__(self):
        self.__spriteBank: Dict[str, List[Image]]   = {}        # 이미지 리소스가 담길 Dictionary.
        self.__spriteResourceSuffix: str            = ".png"    # 이미지 리소스의 확장자.

        self.__bgmBank: Dict[str, Music]            = {}        # BGM 리소스가 담길 Dictionary.
        self.__sfxBank: Dict[str, Wav]              = {}        # SFX 리소스가 담길 Dictionary.
        self.__audioResourceSuffix: str             = '.flac'   # 오디오 리소스의 확장자.

        self.__fontBank: Dict[str, Font]            = {}        # 폰트 리소스가 담길 Dictionary.
        self.__fontResourceSuffix: str              = '.otf'    # 폰트 리소스의 확장자.

    # 이미지 리소스를 로드합니다.
    def LoadSprite(self, _filePath: str) -> Sequence[Image]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_image(str(filePath))

    # 이미지 리소스를 통째로 로드합니다.
    def LoadSprites(self, _directoryPath: str) -> Sequence[Image]:
        directoryPath: Path = Path(_directoryPath)
        if not directoryPath.exists() or not directoryPath.is_dir():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(directoryPath)}\"였습니다.")

        for filePath in directoryPath.iterdir():
            if filePath.is_file() and filePath.suffix() == self.__spriteResourceSuffix:
                yield load_image(str(filePath))

    # BGM 리소스를 로드합니다.
    def LoadBGM(self, _filePath: str) -> Sequence[Music]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_music(str(filePath))

    # SFX 리소스를 로드합니다.
    def LoadSFX(self, _filePath: str) -> Sequence[Wav]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_wav(str(_filePath))

    def LoadFont(self, _filePath: str) ->  Sequence[Font]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_font(str(_filePath))

    # 로드된 스프라이트 리소스를 가져옵니다.
    def GetSprite(self, _key: str, _index: int = 0) -> Image:
        if _key not in self.__spriteBank.keys():
            self.__spriteBank[_key] = []
            for image in self.LoadSprite(_key):
                self.__spriteBank[_key].append(image)

        return self.__spriteBank[_key][_index]

    # 로드된 스프라이트 리소스를 통쨰로 가져옵니다.
    def GetSprites(self, _key: str) -> Sequence[Image]:
        if _key not in self.__spriteBank.keys():
            self.__spriteBank[_key] = []
            for image in self.LoadSprites(_key):
                self.__spriteBank[_key].append(image)

        return self.__spriteBank[_key]

    # 로드된 BGM 리소스를 가져옵니다.
    def GetBGM(self, _key: str) -> Music:
        if _key not in self.__bgmBank.keys():
            for bgm in self.LoadBGM(_key):
                self.__bgmBank[_key] = bgm

        return self.__bgmBank[_key]

    # 로드된 SFX 리소스를 가져옵니다.
    def GetSFX(self, _key: str) -> Wav:
        if _key not in self.__sfxBank.keys():
            for sfx in self.LoadSFX(_key):
                self.__sfxBank[_key] = sfx

        return self.__sfxBank[_key]

    def GetFont(self, _key: str) -> Font:
        if _key not in self.__fontBank.keys():
            for font in self.LoadFont(_key):
                self.__fontBank[_key] = font

        return self.__fontBank[_key]
