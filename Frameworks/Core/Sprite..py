from pico2d import *
from Frameworks.Utilities.FileSystem import *

class Sprite:
    m_image: Image = None   # 이미지
    
    def __init__(self, _filePath: str) -> None:
        self.m_image = GetSprite(_path = _filePath)