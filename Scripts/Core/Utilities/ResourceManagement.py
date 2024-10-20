from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *

from Core.Utilities.Singleton import Singleton

class Sprite:
    def __init__(self, _texture: IMG_INIT_PNG):
        self.__texture: IMG_INIT_PNG    = _texture
        self.__width: int               = c_int()
        self.__height: int              = c_int()

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    def Draw(self, _x: int, _y: int, _width: int , _height: int) -> None:
        ...

    def Draw(self, _x: int, _y: int, _width: int , _height: int, _flipX: bool, _flipY: bool, ) -> None:
        ...

class Audio:
    pass

class BGM(Audio):
    pass

class SFX(Audio):
    pass

class Resources(metaclass = Singleton):
    def __init__(self):
        pass

    def Initialize(self) -> None:
        IMG_Init(IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | IMG_INIT_WEBP)
        TTF_Init()

