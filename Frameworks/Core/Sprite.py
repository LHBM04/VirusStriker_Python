from enum import Enum
from pathlib import Path

from pico2d import *

from Frameworks.Core.Utilities.Mathematics.Color import Color
from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2
from Frameworks.Core.Utilities.ResourceManagement.ResourceManager import ResourceManager


class ELayerLevel(Enum):
    NONE        = 0
    BACKGROUND  = 1
    FOREGROUND  = 2
    OBJECT      = 3
    UI          = 4

class SpriteRI:
    def __init__(self,
                 _position: Vector2         = Vector2(0.0, 0.0),
                 _scale: Vector2            = Vector2(0.0, 0.0),
                 _rotate: float             = 0.0,
                 _isFlipX: bool             = False,
                 _isFlipY: bool             = False,
                 _color: Color              = Color(255.0, 255.0, 255.0, 255.0),
                 _layerLevel: ELayerLevel   = ELayerLevel.NONE) -> None:
        self.position: Vector2              = Vector2()                     # 해당 스프라이트의 위치.
        self.scale: Vector2                 = Vector2()                     # 해당 스프라이트의 크기.
        self.rotate: float                  = 0                             # 해당 스프라이트의 각도.
        self.isFlipX: bool                  = False                         # 해당 스프라이트의 X축 뒤집기 여부.
        self.isFlipY: bool                  = False                         # 해당 스프라이트의 Y축 뒤집기 여부.
        self.color: Color                   = Color()                       # 해당 스프라이트의 R,G,B,A 값
        self.layerLevel: ELayerLevel        = ELayerLevel.NONE              # 해당 스프라이트의 레이어 레벨
        self.renderLayer: int               = 0                             # 해당 스프라이트의 렌더링 순서

class Sprite:
    def __init__(self,
                 _filePath: str,  
                 _isLoop: bool = True) -> None:
        self.info = SpriteRI()                   # 스프라이트 정보

        self.m_textures: list[Image]    = []        # 해당 스프라이트의 텍스쳐들
        self.m_textureSize: int         = 0         # 해당 스프라이트의 텍스쳐 개수.
        self.m_currentTextureIndex: int = 0         # 해당 스프라이트의 현재 텍스쳐.

        self.isLoop: bool                 = _isLoop   # 해당 스프라이트의 루프 여부.
        self.isEnd: bool                  = False     # 해당 스프라이트의 루프 종료 여부.
        self.m_currentAnimateTime: float    = 0.1       # 해당 스프라이트의 애니메이션 시간.
        self.m_animationDeltaTime: float    = 0.0       # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.

        for file in Path(_filePath).iterdir():
            if file.is_file():
                self.m_textures = ResourceManager().GetSprite(_filePath)

        self.m_textureSize = len(self.m_textures)

    # 스프라이트 애니메이션을 업데이트 합니다.
    def Update(self, _deltaTime: float):
            self.m_animationDeltaTime = self.m_animationDeltaTime + _deltaTime

            if self.m_animationDeltaTime > self.m_currentAnimateTime:
                self.m_animationDeltaTime = self.m_animationDeltaTime - self.m_currentAnimateTime
                self.m_currentTextureIndex = self.m_currentTextureIndex + 1

                if self.m_currentTextureIndex >= self.m_textureSize:
                    if self.isLoop:
                        self.m_currentTextureIndex = 0
                    else:
                        self.m_currentTextureIndex = self.m_currentTextureIndex - 1
                        self.isEnd = True

    # 스프라이트를 렌더링합니다.
    def Render(self):
        if self.m_currentTextureIndex >= self.m_textureSize:
            return

        currentTexture: Image   = self.m_textures[self.m_currentTextureIndex]
        x: float                = self.info.position.x
        y: float                = self.info.position.y
        scaleX: float           = self.info.scale.x
        scaleY: float           = self.info.scale.y
        
        # 나중에 3차원 단위 벡터로 해결할 수 있을 듯.
        rotate: float           = self.info.rotate
        isFilp: str             = f"{None if not self.info.isFlipX else 'w'}{None if not self.info.isFlipY else 'h'}"
        
        if (self.info.color.r > 255 or self.info.color.g > 255 or
            self.info.color.b > 255 or self.info.color.a > 255):
            raise ValueError

        currentTexture.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(currentTexture.texture, int(self.info.color.r), int(self.info.color.g), int(self.info.color.b))
        SDL_SetTextureBlendMode(currentTexture.texture, SDL_BLENDMODE_BLEND)
        SDL_SetTextureAlphaMod(currentTexture.texture, int(self.info.color.a))