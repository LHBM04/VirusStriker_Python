from ctypes import *
from numpy import *
from typing import *

from multipledispatch import dispatch
from sdl2 import *

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject
from Core.SystemManagement import SystemManager

@final
class Sprite:
    def __init__(self, _texture: SDL_Texture):
        self.__texture: SDL_Texture = _texture

        width: c_int    = c_int(0)
        height: c_int   = c_int(0)

        SDL_QueryTexture(self.__texture, None, None, byref(width), byref(height))

        self.__point    = SDL_Point(width.value // 2, height.value // 2)
        self.__rect     = SDL_Rect(0, 0, width.value, height.value)

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

@final
class SpriteRenderer(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)
        
        self.__texture: Optional[SDL_Texture]   = None
        self.__color: SDL_Color                 = SDL_Color(255, 255, 255, 255)
        self.__flipFlag: int                    = SDL_FLIP_NONE

        self.__rect: SDL_Rect                   = SDL_Rect()
        self.__point: SDL_Point                 = SDL_Point()

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

        width: c_int    = c_int(0)
        height: c_int   = c_int(0)
        SDL_QueryTexture(self.__texture, None, None, byref(width), byref(height))

        self.__point    = SDL_Point(width.value // 2, height.value // 2)
        self.__rect     = SDL_Rect(0, 0, width.value, height.value)

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

    @dispatch(int, int)
    def Draw(self, _x: int, _y: int) -> None:
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, self.__rect, 0.0, self.__point, self.__flipFlag)

    @dispatch(int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int) -> None:
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, self.__rect, degrees(-_rotate), self.__point, self.__flipFlag)