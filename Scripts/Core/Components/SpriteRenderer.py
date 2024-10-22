from ctypes import *
from numpy import *
from typing import *

from multipledispatch import dispatch
from sdl2 import *

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject
from Core.SystemManagement import SystemManager

@final
class SpriteRenderer(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)
        
        self.__texture: Optional[SDL_Texture]   = None
        self.__color: SDL_Color                 = SDL_Color(255, 255, 255, 255)
        self.__flipFlag: int                    = SDL_FLIP_NONE

        self.__width: c_int                     = c_int(0)
        self.__height: c_int                    = c_int(0)
        self.__rect: SDL_Rect                   = SDL_Rect()

        self.__sortingLayer: int                = 0
        self.__orderInLayer: int                = 0

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    # region Properties
    @property
    def texture(self) -> SDL_Texture:
        return self.__texture

    @texture.setter
    def texture(self, _value: SDL_Texture) -> None:
        self.__texture = _value
        SDL_QueryTexture(self.__texture, None, None, byref(self.__width), byref(self.__height))

    @property
    def color(self) -> SDL_Color:
        return self.__color

    @color.setter
    def color(self, _value: SDL_Color) -> None:
        self.__color = _value

    @property
    def flipX(self) -> bool:
        return (self.__flipFlag & SDL_FLIP_HORIZONTAL) == SDL_FLIP_HORIZONTAL

    @flipX.setter
    def flipX(self, _value: bool) -> None:
        if _value:
            self.__flipFlag |= SDL_FLIP_HORIZONTAL

        else:
            self.__flipFlag &= ~SDL_FLIP_HORIZONTAL

    @property
    def flipY(self) -> bool:
        return (self.__flipFlag & SDL_FLIP_VERTICAL) == SDL_FLIP_VERTICAL

    @flipY.setter
    def flipY(self, _value: bool) -> None:
        if _value:
            self.__flipFlag |= SDL_FLIP_VERTICAL

        else:
            self.__flipFlag &= ~SDL_FLIP_VERTICAL

    @property
    def sortingLayer(self) -> int:
        return self.__sortingLayer

    @sortingLayer.setter
    def sortingLayer(self, _value: int) -> None:
        self.__sortingLayer = _value

    @property
    def orderInLayer(self) -> int:
        return self.__orderInLayer

    @orderInLayer.setter
    def orderInLayer(self, _value: int) -> None:
        self.__orderInLayer = _value
    # endregion

    def __InitSDLRect(self, _x: int, _y: int, _w: int, _h: int) -> SDL_Rect:
        return SDL_Rect(int(_x), int(-_y + SystemManager().windowHeight - _h), int(_w), int(_h))

    @dispatch(int, int)
    def Draw(self, _x: int, _y: int) -> None:
        rectangle: SDL_Rect = self.__InitSDLRect(_x - self.__width // 2, _y - self.__height // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rectangle, 0.0, None, self.__flipFlag)

    @dispatch(int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int) -> None:
        rectangle: SDL_Rect = self.__InitSDLRect((_x - self.__width) // 2, (_y - self.__height) // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rectangle, degrees(-_rotate), None, SDL_FLIP_NONE)

    @dispatch(int, int, int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int, _width: int, _height: int, _flipX: bool, _flipY: bool) -> None:
        rectangle: SDL_Rect  = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        flipFlag: int   = ((SDL_FLIP_VERTICAL if _flipX else SDL_FLIP_NONE) | (SDL_FLIP_HORIZONTAL if _flipY else SDL_FLIP_NONE))

        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rectangle, degrees(-_rotate), None, flipFlag)