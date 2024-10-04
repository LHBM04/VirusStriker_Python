from pathlib import Path
from typing import Dict, Iterator, List, final

from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton

def MakePath(_path: str) -> Path:
    return Path(_path)

@final
class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self._spriteBank: Dict[str, list[Image]] = {}
        self.__spriteFileSuffix: str = ".str"

        self._bgmBank: Dict[str, Music] = {}
        self._sfxBank: Dict[str, Wav] = {}
        self.__audioFileSuffix: str = '.wav'

    def LoadSprite(self, _filePath: Path) -> Iterator[Image]:
        if not _filePath.exists() or not _filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(_filePath)}\"였습니다.")

        yield load_image(str(_filePath))

    def LoadSprites(self, _directoryPath: Path) -> Iterator[Image]:
        if not _directoryPath.exists() or not _directoryPath.is_dir():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(_directoryPath)}\"였습니다.")

        for filePath in _directoryPath.iterdir():
            if filePath.is_file():
                yield load_image(str(filePath))

    def LoadBGM(self, _filePath: Path) -> Iterator[Music]:
        if not _filePath.exists() or not _filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(_filePath)}\"였습니다.")

        yield load_music(str(_filePath))

    def LoadSFX(self, _filePath: Path) -> Iterator[Wav]:
        if not _filePath.exists() or not _filePath.is_file():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(_filePath)}\"였습니다.")

        yield load_wav(str(_filePath))

    def GetSprite(self, _key: str, _index: int = 0) -> Image:
        if _key not in self._spriteBank.keys():
            self._spriteBank[_key] = []
            for image in self.LoadSprite(MakePath(_key)):
                self._spriteBank[_key].append(image)

        return self._spriteBank[_key][_index]

    def GetImages(self, _key: str) -> List[Image]:
        if _key not in self._spriteBank.keys():
            self._spriteBank[_key] = []
            for image in self.LoadSprites(MakePath(_key)):
                self._spriteBank[_key].append(image)

        return self._spriteBank[_key]

    def GetBGM(self, _key: str) -> Music:
        if _key not in self._bgmBank.keys():
            for bgm in self.LoadBGM(MakePath(_key)):
                self._bgmBank[_key] = bgm

        return self._bgmBank[_key]

    def GetSFX(self, _key: str) -> Wav:
        if _key not in self._sfxBank.keys():
            for sfx in self.LoadSFX(MakePath(_key)):
                self._sfxBank[_key] = sfx

        return self._sfxBank[_key]
