from ctypes import *
from typing import *

from sdl2 import *
from sdl2.sdlimage import *

from Core.Objects.Object import Object

@final
class Sprite(Object):
    def __init__(self, _texture: SDL_Texture):
        super().__init__()
        
        self.__texture: SDL_Texture = _texture

        width: c_int    = c_int(0)
        height: c_int   = c_int(0)

        SDL_QueryTexture(self.__texture, None, None, byref(width), byref(height))

        self.__pivot    = SDL_Point(width.value // 2, height.value // 2)
        self.__rect     = SDL_Rect(0, 0, width.value, height.value)

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    # region Properties
    @property
    def texture(self) -> SDL_Texture:
        return self.__texture

    @property
    def pivot(self) -> SDL_Point:
        return self.__pivot

    @pivot.setter
    def pivot(self, _value: SDL_Point) -> None:
        self.__pivot = _value

    @property
    def rect(self) -> SDL_Rect:
        return self.__rect
    # endregion