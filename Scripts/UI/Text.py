from ctypes import c_byte
from typing import Optional, AnyStr

from sdl2 import *
from sdl2.sdlttf import *

from Core.Objects.Font import Font
from Core.SystemManagement import SystemManager

class Text:
    def __init__(self):
        self.__font: Optional[Font] = None
        self.__text: AnyStr         = ""
        self.__scale: int           = 8
        self.__color: SDL_Color     = SDL_Color(255, 255, 255, 255)

    def __del__(self):
        ...

    @property
    def text(self) -> AnyStr:
        return self.__text

    @text.setter
    def text(self, _value: AnyStr) -> None:
        self.__text = _value

    def Render(self) -> None:
        surface: SDL_Surface = TTF_RenderText_Solid(self.__font.font, self.__text.encode('UTF-8'), self.__color)
        texture: SDL_Texture = SDL_CreateTextureFromSurface(SystemManager().rendererHandle, surface)

        width: c_int = c_int(0)
        height: c_int = c_int(0)
        SDL_QueryTexture(texture, None, None, c_byte.byref(width), c_byte.byref(height))
        center = SDL_Point(width.value // 2, height.value // 2)
        rectangle = SDL_Rect(1000, 10, width.value, height.value)

        SDL_RenderCopyEx(SystemManager().rendererHandle, texture, None, rectangle, 0.0, center, 0)
