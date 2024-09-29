from pico2d import *
from Utilities.FileSystem import *
from typing import List
from io import *
from pathlib import Path

class Sprite:
    def __init__(self, _dirPath: str) -> None:
        self.m_textures: List[Image]    = []    # 해당 스프라이트의 텍스쳐들
        self.m_textureSize: int         = 0     # 해당 스프라이트의 텍스쳐 개수.
        self.m_currentTextureIndex: int = 0     # 해당 스프라이트의 현재 텍스쳐.

        self.m_anyLoop: bool        = True  # 루프 여부
        self.m_aniTime: float       = 0.1   # 애니메이션 시간.
        self.m_aniDeltaTime: float  = 0.0   # 애니메이션에 사용될 타이머.
        
        for file in Path(_dirPath).iterdir():
            if file.is_file():
                self.m_textures.append(GetSprite(str(file))) 

        self.m_textureSize = len(self.m_textures)

    def Update(self, _deltaTime: float):
        self.m_aniDeltaTime = self.m_aniDeltaTime + _deltaTime

        if self.m_aniDeltaTime > self.m_aniTime:
            self.m_aniDeltaTime = self.m_aniDeltaTime - self.m_aniTime
            self.m_currentTextureIndex = self.m_currentTextureIndex + 1

            if self.m_currentTextureIndex >= self.m_textureSize:
                if self.m_anyLoop:
                    self.m_currentTextureIndex = 0
                else:
                    self.m_currentTextureIndex = self.m_currentTextureIndex - 1

    def Render(self):
        if self.m_currentTextureIndex >= self.m_textureSize:
            assert(0)
            return
        
        currentTexture: Image = self.m_textures[self.m_currentTextureIndex]
        currentTexture.composite_draw(0, '', 1280 / 2, 800 / 2, None, None)