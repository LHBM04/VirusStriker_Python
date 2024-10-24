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
        
        self.__sprite: Optional[Sprite]         = None
        self.__color: SDL_Color                 = SDL_Color(255, 255, 255, 255)
        self.__flipFlag: int                    = SDL_FLIP_NONE

        self.__rect: SDL_Rect                   = SDL_Rect()
        self.__point: SDL_Point                 = SDL_Point()

        self.__sortingLayer: int                = 0
        self.__orderInLayer: int                = 0

    def __del__(self):
        SDL_DestroyTexture(self.__sprite)

    # region Properties
    @property
    def sprite(self) -> Sprite:
        return self.__sprite

    @sprite.setter
    def sprite(self, _value: Sprite) -> None:
        self.__sprite = _value

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
    def Draw(self, _x: int, _y: int, _rotate: int = 0) -> None:
        SDL_RenderCopyEx(
            SystemManager().rendererHandle,
            self.__sprite.texture,
            self.__sprite.rect,
            self.__sprite.rect,
            degrees(-_rotate),
            self.__sprite.pivot,
            self.__flipFlag)
        SDL_SetTextureColorMod(self.__sprite.texture, self.__color.r, self.__color.g, self.__color.b)
        SDL_SetTextureAlphaMod(self.__sprite.texture, self.__color.a)
        SDL_SetTextureBlendMode(self.__sprite.texture, SDL_BLENDMODE_BLEND)