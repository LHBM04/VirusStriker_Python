from argparse import ArgumentError
from enum import Enum
from multipledispatch import dispatch

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

class Sprite:
    @dispatch(Image)
    def __init__(self, _texture: Image) -> None:
        if _texture is None:
            raise ArgumentError

        self.textures: Image            = _texture
        self.position: Vector2          = Vector2(0.0, 0.0)  # 해당 스프라이트의 위치.
        self.scale: Vector2             = Vector2(0.0, 0.0)  # 해당 스프라이트의 크기.
        self.rotate: float              = 0  # 해당 스프라이트의 각도.
        self.isFlipX: bool              = False  # 해당 스프라이트의 X축 뒤집기 여부.
        self.isFlipY: bool              = False  # 해당 스프라이트의 Y축 뒤집기 여부.
        self.color: Color               = Color(255, 255, 255, 255)  # 해당 스프라이트의 R,G,B,A 값
        self.layerLevel: ELayerLevel    = ELayerLevel.NONE  # 해당 스프라이트의 레이어 레벨
        self.renderLayer: int           = 0  # 해당 스프라이트의 렌더링 순서

    @dispatch(str)
    def __init__(self, _path: str) -> None:
        if _path is None or _path.isspace():
            raise ArgumentError

        self.textures: Image            = ResourceManager().LoadSprite(_path)
        self.position: Vector2          = Vector2(0.0, 0.0)  # 해당 스프라이트의 위치.
        self.scale: Vector2             = Vector2(0.0, 0.0)  # 해당 스프라이트의 크기.
        self.rotate: float              = 0  # 해당 스프라이트의 각도.
        self.isFlipX: bool              = False  # 해당 스프라이트의 X축 뒤집기 여부.
        self.isFlipY: bool              = False  # 해당 스프라이트의 Y축 뒤집기 여부.
        self.color: Color               = Color(255, 255, 255, 255)  # 해당 스프라이트의 R,G,B,A 값
        self.layerLevel: ELayerLevel    = ELayerLevel.NONE  # 해당 스프라이트의 레이어 레벨
        self.renderLayer: int           = 0  # 해당 스프라이트의 렌더링 순서

    # 스프라이트를 렌더링합니다.
    def Render(self):
        x: float                = self.position.x
        y: float                = self.position.y
        scaleX: float           = self.scale.x
        scaleY: float           = self.scale.y
        rotate: float           = self.rotate
        isFilp: str             = f"{None if not self.isFlipX else 'w'}{None if not self.isFlipY else 'h'}"
        
        if (self.color.r > Color.MaxValue() or self.color.g > Color.MaxValue() or
            self.color.b > Color.MaxValue() or self.color.a > Color.MaxValue()):
            raise ValueError

        self.textures.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(self.textures.texture, int(self.color.r), int(self.color.g), int(self.color.b))
        SDL_SetTextureAlphaMod(self.textures.texture, int(self.color.a))
        SDL_SetTextureBlendMode(self.textures.texture, SDL_BLENDMODE_BLEND)
