from pathlib import Path
from typing import Dict, Iterator, List, final

from pico2d import *

from Core.Utilities.Singleton import Singleton

@final
class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self._spriteBank: Dict[str, List[Image]] = {}
        self.__spriteFileSuffix: str = ".str"

        self._bgmBank: Dict[str, Music] = {}
        self._sfxBank: Dict[str, Wav] = {}
        self.__audioFileSuffix: str = '.wav'

    def LoadSprite(self, _filePath: str) -> Iterator[Image]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_image(str(filePath))

    def LoadSprites(self, _directoryPath: str) -> Iterator[Image]:
        directoryPath: Path = Path(_directoryPath)
        if not directoryPath.exists() or not directoryPath.is_dir():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(directoryPath)}\"였습니다.")

        for filePath in directoryPath.iterdir():
            if filePath.is_file():
                yield load_image(str(filePath))

    def LoadBGM(self, _filePath: str) -> Iterator[Music]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_music(str(filePath))

    def LoadSFX(self, _filePath: str) -> Iterator[Wav]:
        filePath: Path = Path(_filePath)
        if not filePath.exists() or not filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield load_wav(str(_filePath))

    def GetSprite(self, _key: str, _index: int = 0) -> Image:
        if _key not in self._spriteBank.keys():
            self._spriteBank[_key] = []
            for image in self.LoadSprite(_key):
                self._spriteBank[_key].append(image)

        return self._spriteBank[_key][_index]

    def GetSprites(self, _key: str) -> List[Image]:
        if _key not in self._spriteBank.keys():
            self._spriteBank[_key] = []
            for image in self.LoadSprites(_key):
                self._spriteBank[_key].append(image)

        return self._spriteBank[_key]

    def GetBGM(self, _key: str) -> Music:
        if _key not in self._bgmBank.keys():
            for bgm in self.LoadBGM(_key):
                self._bgmBank[_key] = bgm

        return self._bgmBank[_key]

    def GetSFX(self, _key: str) -> Wav:
        if _key not in self._sfxBank.keys():
            for sfx in self.LoadSFX(_key):
                self._sfxBank[_key] = sfx

        return self._sfxBank[_key]