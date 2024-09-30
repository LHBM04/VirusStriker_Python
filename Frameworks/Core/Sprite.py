from io import *
from pathlib import Path

from pico2d import *

from Utilities.Vector2 import *
from Utilities.FileManagement import *

# 게임 내 사용될 스프라이트의 컬러 데이터.
@final
class Color:
    @staticmethod
    def minValue() -> int:
        return 0
    
    @staticmethod
    def maxValue() -> int:
        return 255
    
    def __init__(self, 
                 _r: int = maxValue(), 
                 _g: int = maxValue(), 
                 _b: int = maxValue(), 
                 _a: int = maxValue()) -> None:
        self.r = max(self.minValue(), min(_r, self.maxValue()))
        self.g = max(self.minValue(), min(_g, self.maxValue()))
        self.b = max(self.minValue(), min(_b, self.maxValue()))
        self.a = max(self.minValue(), min(_a, self.maxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return self.r == _other.r and self.g == _other.g and self.b == _other.b and self.a == _other.a

    def __ne__(self, _other: 'Color') -> bool:
        return not self.__eq__(_other)

# 스프라이트 정보
class SpriteInfo:
    def __init__(self, 
                 _position: Vector2 = Vector2(), 
                 _scale: Vector2    = Vector2(), 
                 _rotate: float     = 0.0, 
                 _isFlipX: bool     = False, 
                 _isFlipY: bool     = False, 
                 _color: Color      = Color()) -> None:
        self.position: Vector2    = _position               # 해당 스프라이트의 위치.
        self.scale: Vector2       = _scale                  # 해당 스프라이트의 크기.
        self.rotate: float        = _rotate                 # 해당 스프라이트의 각도.
        self.isFlip: list[bool]   = [_isFlipX, _isFlipY]    # 해당 스프라이트의 뒤집기 여부.
        self.color: Color         = _color                  # 해당 스프라이트의 R,G,B,A 값

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
        x: float                = _info.position.x
        y: float                = _info.position.y
        scaleX                  = _info.scale.x
        scaleY                  = _info.scale.y

        currentTexture.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(currentTexture.texture, _info.color.r, _info.color.g, _info.color.b)
        SDL_SetTextureAlphaMod(currentTexture.texture, _info.color.a)