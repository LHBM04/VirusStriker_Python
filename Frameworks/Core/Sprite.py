from io import *
from pathlib import Path

from pico2d import *

from Core.Vector2 import *
from Utilities.FileSystem import *

# 게임 내 사용될 스프라이트의 컬러 데이터.
@final
class Color:
    MIN_COLOR_VALUE: int = 0    # 컬러 최솟값.
    MAX_COLOR_VALUE: int = 255  # 컬러 최댓값.
    
    def __init__(self, 
                 _r: int = MAX_COLOR_VALUE, 
                 _g: int = MAX_COLOR_VALUE, 
                 _b: int = MAX_COLOR_VALUE, 
                 _a: int = MAX_COLOR_VALUE) -> None:
        self.r = max(self.MIN_COLOR_VALUE, min(_r, self.MAX_COLOR_VALUE))
        self.g = max(self.MIN_COLOR_VALUE, min(_g, self.MAX_COLOR_VALUE))
        self.b = max(self.MIN_COLOR_VALUE, min(_b, self.MAX_COLOR_VALUE))
        self.a = max(self.MIN_COLOR_VALUE, min(_a, self.MAX_COLOR_VALUE))

# 
class SpriteInfo:
    def __init__(self, 
                 _position: Vector2 = Vector2(), 
                 _scale: Vector2    = Vector2(100, 100), 
                 _rotate: float     = 0.0, 
                 _isFilpX: bool     = False, 
                 _isFlipY: bool     = False, 
                 _color: Color      = None) -> None:
        self.position: Vector2    = _position if _position is not None else Vector2(0.0, 0.0)   # 해당 스프라이트의 위치.
        self.scale: Vector2       = _scale if _scale is not None else Vector2(100, 100)         # 해당 스프라이트의 크기.
        self.rotate: float        = _rotate                                                     # 해당 스프라이트의 각도.
        self.isFlip: list[bool]   = [_isFilpX, _isFlipY]                                        # 해당 스프라이트의 플립 여부.
        self.color: Color         = _color if _color is not None else Color()

class Sprite:
    def __init__(self, 
                 _filePath: str,  
                 _isLoop: bool = True) -> None:
        self.m_textures: list[Image]    = []    # 해당 스프라이트의 텍스쳐들
        self.m_textureSize: int         = 0     # 해당 스프라이트의 텍스쳐 개수.
        self.m_currentTextureIndex: int = 0     # 해당 스프라이트의 현재 텍스쳐.

        self.m_isLoop: bool                 = _isLoop   # 루프 여부
        self.m_currentAnimateTime: float    = 0.1       # 애니메이션 시간.
        self.m_animationDeltaTime: float    = 0.0       # 애니메이션에 사용될 타이머.
        
        for file in Path(_filePath).iterdir():
            if file.is_file():
                self.m_textures = FileManager().GetSprite(_filePath)

        self.m_textureSize = len(self.m_textures)

    # 스프라이트 애니메이션을 업데이트 합니다.
    def Update(self, _deltaTime: float):
        self.m_animationDeltaTime = self.m_animationDeltaTime + _deltaTime

        if self.m_animationDeltaTime > self.m_currentAnimateTime:
            self.m_animationDeltaTime = self.m_animationDeltaTime - self.m_currentAnimateTime
            self.m_currentTextureIndex = self.m_currentTextureIndex + 1

            if self.m_currentTextureIndex >= self.m_textureSize:
                if self.m_isLoop:
                    self.m_currentTextureIndex = 0
                else:
                    self.m_currentTextureIndex = self.m_currentTextureIndex - 1

    # 스프라이트를 렌더링합니다.
    def Render(self, _info: SpriteInfo):
        if self.m_currentTextureIndex >= self.m_textureSize:
            assert(0)
            return
        
        currentTexture: Image   = self.m_textures[self.m_currentTextureIndex]
        rotate: float           = _info.rotate
        isFilp: str             = f"{None if not _info.isFlip[0] else 'w'}{None if not _info.isFlip[1] else 'h'}"
        x: float                = _info.position.m_x
        y: float                = _info.position.m_y
        scaleX                  = _info.scale.m_x
        scaleY                  = _info.scale.m_y

        currentTexture.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(currentTexture.texture, _info.color.r, _info.color.g, _info.color.b)
        SDL_SetTextureAlphaMod(currentTexture.texture, _info.color.a)