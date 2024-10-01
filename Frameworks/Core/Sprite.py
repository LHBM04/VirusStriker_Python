from io import *
from pathlib import Path
from enum import Enum

from pico2d import *

from sdl2 import *
from sdl2dll import *

from Utilities.Color import *
from Utilities.Vector2 import *
from Utilities.ResourceManagement import *

class Sprite:
    class Info:
        class ELevel(Enum):
            NONE        = 0
            BACKGROUND  = 1
            FOREGROUND  = 2
            OBJECT      = 3
            UI          = 4

        def __init__(self) -> None:
            self.position: Vector2              = Vector2()               # 해당 스프라이트의 위치.
            self.scale: Vector2                 = Vector2()                  # 해당 스프라이트의 크기.
            self.rotate: float                  = float                 # 해당 스프라이트의 각도.
            self.isFlip: list[bool]             = [False, False]    # 해당 스프라이트의 뒤집기 여부.
            self.color: Color                   = Color()                  # 해당 스프라이트의 R,G,B,A 값
            self.layerLevel: Sprite.Info.ELevel = Sprite.Info.ELevel.NONE
            self.renderLayer: int               = 0
    
    def __init__(self, 
                 _owner: 'Object',
                 _filePath: str,  
                 _isLoop: bool = True) -> None:
        self.owner: 'Object'            = _owner      # 스프라이트 주인
        self.info = Sprite.Info()                   # 스프라이트 정보

        self.m_textures: list[Image]    = []        # 해당 스프라이트의 텍스쳐들
        self.m_textureSize: int         = 0         # 해당 스프라이트의 텍스쳐 개수.
        self.m_currentTextureIndex: int = 0         # 해당 스프라이트의 현재 텍스쳐.

        self.m_isLoop: bool                 = _isLoop   # 루프 여부
        self.m_currentAnimateTime: float    = 0.1       # 애니메이션 시간.
        self.m_animationDeltaTime: float    = 0.0       # 애니메이션에 사용될 타이머.
        
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
                if self.m_isLoop:
                    self.m_currentTextureIndex = 0
                else:
                    self.m_currentTextureIndex = self.m_currentTextureIndex - 1

    # 스프라이트를 렌더링합니다.
    def Render(self):
        if self.m_currentTextureIndex >= self.m_textureSize:
            return

        currentTexture: Image   = self.m_textures[self.m_currentTextureIndex]
        x: float                = self.owner.position.x
        y: float                = self.owner.position.y
        scaleX: float           = self.owner.scale.x
        scaleY: float           = self.owner.scale.y
        
        # 나중에 3차원 단위 벡터로 해결할 수 있을 듯.
        rotate: float           = self.owner.rotate
        isFilp: str             = f"{None if not self.info.isFlip[0] else 'w'}{None if not self.info.isFlip[1] else 'h'}"
        
        if (self.info.color.r > 255 or self.info.color.g > 255 or
            self.info.color.b > 255 or self.info.color.a > 255):
            assert("[Oops!] 컬러값이 이상해요")
            return

        currentTexture.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(currentTexture.texture, int(self.info.color.r), int(self.info.color.g), int(self.info.color.b))
        SDL_SetTextureBlendMode(currentTexture.texture, SDL_BLENDMODE_BLEND)
        SDL_SetTextureAlphaMod(currentTexture.texture, int(self.info.color.a))
        
from Core.Actors.Object import *