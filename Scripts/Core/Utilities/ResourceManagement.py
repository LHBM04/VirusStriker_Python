from abc import ABCMeta, abstractmethod
from typing import final, Dict, Optional, Sequence, List

from pathlib import *
from pico2d import *

from Core.Components.Transform import Transform
from Core.Utilities.Singleton import Singleton

class Resource(metaclass = ABCMeta):
    """
    게임 내 사용되는 모든 리소스의 베이스 클래스.
    """
    @classmethod
    @abstractmethod
    def fileSuffix(cls) -> str:
        """
        해당 리소스의 확장자 명을 반환합니다.
        :return: 해당 리소스의 확장자 명.
        """
        raise NotImplementedError("[Oops!] 해당 함수/메서드/프로퍼티가 정의되지 않았습니다!")

@final
class Sprite(Resource):
    """
    게임 내 사용되는 Sprite를 정의합니다.
    """
    def __init__(self, _image: Image = None):
        self.__image: Optional[Image] = None

    @classmethod
    def fileSuffix(cls) -> str:
        """
        해당 리소스의 확장자 명을 반환합니다.
        :return: 해당 리소스의 확장자 명.
        """
        return '.png'

    def Render(self,
               _transform: Transform,
               _color: SDL_Color,
               _isFlipX: bool = False,
               _isFlipY: bool = False):
        if self.__image is None:
            raise ValueError("[Oops!] 렌더링할 Texture가 존재하지 않습니다.")

        self.__image.composite_draw(_transform.rotation,
                                    ('w' if _isFlipX else '') + ('h' if _isFlipY else ''),
                                    _transform.position.x,
                                    _transform.position.y,
                                    _transform.scale.x,
                                    _transform.scale.y)
        SDL_SetTextureColorMod(self.__image.texture, _color.r, _color.g, _color.b)  # 색상 정보 수정
        SDL_SetTextureAlphaMod(self.__image.texture, _color.a)
        SDL_SetTextureBlendMode(self.__image.texture, SDL_BLENDMODE_BLEND)

@final
class BGM(Resource):
    """
    게임 내 사용되는 BGM을 정의합니다.
    """
    @classmethod
    def fileSuffix(cls) -> str:
        """
        해당 리소스의 확장자 명을 반환합니다.
        :return: 해당 리소스의 확장자 명.
        """
        return ".flac"


@final
class SFX(Resource):
    """
    게임 내 사용되는 SFX를 정의합니다.
    """
    @classmethod
    def fileSuffix(cls) -> str:
        """
        해당 리소스의 확장자 명을 반환합니다.
        :return: 해당 리소스의 확장자 명.
        """
        return ".flac"

@final
class ResourceManager(metaclass = Singleton):
    """
    게임 내 사용되는 리소스를 일기 및 저장합니다.
    """
    def __init__(self):
        self.__spriteBank: Dict[str, List[Sprite]]  = {}    # 읽어온 Sprite를 이곳에 경로와 함께 저장합니다.
        self.__bgmBank: Dict[str, BGM]              = {}    # 읽어온 BGM을 이곳에 경로와 함께 저장합니다.
        self.__sfxBank: Dict[str, SFX]              = {}    # 읽어온 SFX를 이곳에 경로와 함께 저장합니다.
        self.__fontBank: Dict[str, Font]            = {}    # 읽어온 Font를 이곳에 경로와 함께 저장합니다.

    # region Resource Loader
    def LoadSprite(self, _filePath: str) -> Sequence[Sprite]:
        """
        Sprite 리소스를 읽어옵니다.
        :param _filePath: Sprite 리소스의 파일 경로.
        :return: 읽어온 Sprite 리소스.
        """
        filePath: Path = Path(_filePath)
        if (not filePath.exists() or
            not filePath.is_file()):
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        elif filePath.suffix != Sprite.fileSuffix():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(filePath)}\"였습니다.")

        yield Sprite(load_image(str(filePath)))

    def LoadSprites(self, _directoryPath: str) -> Sequence[Sprite]:
        """
        Sprite 리소스들을 읽어옵니다.
        :param _directoryPath: Sprite 리소스의 폴더 경로.
        :return: 읽어온 Sprite 리소스들.
        """
        directoryPath: Path = Path(_directoryPath)
        if not directoryPath.exists() or not directoryPath.is_dir():
            raise IOError(f"[Oops!] 해당 경로는 존재하지 않거나 허용되지 않습니다! 경로는 \"{str(directoryPath)}\"였습니다.")

        for filePath in directoryPath.iterdir():
            yield self.LoadSprite(str(filePath))
    # endregion
    # region Resource Getter
    # 로드된 스프라이트 리소스를 가져옵니다.
    def GetSprite(self, _key: str, _index: int = 0) -> Sprite:
        """
        불러온 Sprite 리소스를 반환합니다.\n
        (※ 보통 한 장만 있는 Sprite를 가져오는 용도로 사용됩니다.)
        :param _key: 불러온 Sprite 리소스의 경로.
        :param _index: 불러온 Sprite 리소스의 인덱스 번호.
        :return: 불러온 Sprite 리소스.
        """
        if _key not in self.__spriteBank.keys():
            self.__spriteBank[_key] = []
            for image in self.LoadSprite(_key):
                self.__spriteBank[_key].append(image)

        return self.__spriteBank[_key][_index]

        # 로드된 스프라이트 리소스를 통쨰로 가져옵니다.

    def GetSprites(self, _key: str) -> Sequence[Sprite]:
        """
        불러온 Sprite를을 반환합니다.
        :param _key: 불러온 Sprite 리소스의 경로.
        :return: 불러온 Sprite 리소스들.
        """
        if _key not in self.__spriteBank:
            self.__spriteBank[_key] = []
            for image in self.LoadSprites(_key):
                self.__spriteBank[_key].append(image)

        return self.__spriteBank[_key]
    # endregion