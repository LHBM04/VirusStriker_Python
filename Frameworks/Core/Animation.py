from argparse import ArgumentError
from enum import Enum

from pico2d import *

from Frameworks.Core.Utilities.Mathematics.Color import Color
from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2

class Animation:
    def __init__(self, _texture: list[Image]) -> None:
        if _texture is None:
            raise ArgumentError

        self.m_textures: list[Image]    = []                    # 해당 스프라이트의 텍스쳐들
        self.m_currentTextureIndex: int = 0                     # 해당 스프라이트의 현재 텍스쳐 인덱스.
        self.renderInfo                 = SpriteRI()            # 스프라이트 정보

        self.isLoop: bool                   = _isLoop           # 해당 스프라이트의 루프 여부.
        self.isEnd: bool                    = False             # 해당 스프라이트의 루프 종료 여부.
        self.m_currentAnimateTime: float    = 0.1               # 해당 스프라이트의 애니메이션 시간.
        self.m_animationDeltaTime: float    = 0.0               # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.

        self.m_textures.append(_texture)
        self.m_textureSize: int         = len(self.m_textures)  # 해당 스프라이트의 텍스쳐 개수.