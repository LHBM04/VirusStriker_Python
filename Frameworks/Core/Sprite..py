from pico2d import *
from Utilities.FileSystem import *

class Sprite:
    m_texture: Image = None   # 택스쳐
    m_anyLoop: bool = True    # 루프 여부
    
    def __init__(self, _filePath: str) -> None:
        self.m_texture = GetSprite(_path = _filePath)

    def Render():
        pass
