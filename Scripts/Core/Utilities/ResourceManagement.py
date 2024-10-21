from math import *
from typing import *

from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *

from Core.SystemManagement import System
from Core.Utilities.Singleton import Singleton

@final
class Sprite:
    def __init__(self, _texture: IMG_INIT_PNG):
        self.__texture: IMG_INIT_PNG    = _texture
        self.__width: c_int             = c_int()
        self.__height: c_int            = c_int()

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    def __InitSDLRect(self, _x: int, _y: int, _w: int, _h: int) -> SDL_Rect:
        return SDL_Rect(int(_x), int(-_y + System().windowHeight - _h), int(_w), int(_h))

    @overload
    def Draw(self, _x: int, _y: int, _rotate: int) -> None:
        ...

    def Draw(self, _x: int, _y: int, _rotate: int, _width: Optional[int] = None, _height: Optional[int] = None, _flipX: bool = False, _flipY: bool = False) -> None:
        if _width is None and _height is None:
            _width, _height = self.__width, self.__height


        rect: SDL_Rect = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        flipFlag: int = (SDL_FLIP_VERTICAL if _flipX else SDL_FLIP_NONE) | (SDL_FLIP_HORIZONTAL if _flipY else SDL_FLIP_NONE)

        SDL_RenderCopyEx(System().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, flipFlag)

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

