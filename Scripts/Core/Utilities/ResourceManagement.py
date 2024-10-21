from numpy import *
from typing import *

from multipledispatch import dispatch
from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
from sdl2.sdlmixer import *

from Core.SystemManagement import SystemManager
from Core.Utilities.Singleton import Singleton

@final
class Sprite:
    def __init__(self, _texture: SDL_Texture):
        self.__texture: SDL_Texture     = _texture
        self.__width: int               = 0
        self.__height: int              = 0

    def __del__(self):
        SDL_DestroyTexture(self.__texture)

    def __InitSDLRect(self, _x: int, _y: int, _w: int, _h: int) -> SDL_Rect:
        return SDL_Rect(int(_x), int(-_y + SystemManager().windowHeight - _h), int(_w), int(_h))

    @dispatch(int, int)
    def Draw(self, _x: int, _y: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - self.__width) // 2, (_y - self.__height) // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, 0.0, None, SDL_FLIP_NONE)

    @dispatch(int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - self.__width) // 2, (_y - self.__height) // 2, self.__width, self.__height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, SDL_FLIP_NONE)

    @dispatch(int, int, int, int, int)
    def Draw(self, _x: int, _y: int, _rotate: int, _width: int, _height: int) -> None:
        rect: SDL_Rect = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, SDL_FLIP_NONE)

    @dispatch(int, int, int, int, int, bool, bool)
    def Draw(self, _x: int, _y: int, _rotate: int, _width: int, _height: int, _flipX: bool, _flipY: bool) -> None:
        rect: SDL_Rect  = self.__InitSDLRect((_x - _width) // 2, (_y - _height) // 2, _width, _height)
        flipFlag: int   = ((SDL_FLIP_VERTICAL if _flipX else SDL_FLIP_NONE) | (SDL_FLIP_HORIZONTAL if _flipY else SDL_FLIP_NONE))

        SDL_RenderCopyEx(SystemManager().rendererHandle, self.__texture, None, rect, degrees(-_rotate), None, flipFlag)

class ResourceManager(metaclass = Singleton):
    def __init__(self):
        self.__textureBank: Dict[str, SDL_Texture]  = { }
        self.__bgmBank: Dict[str, Mix_Music]        = { }
        self.__sfxBank: Dict[str, Mix_Music]        = { }
        self.__ttfBank: Dict[str, TTF_Font]         = { }

        IMG_Init(IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | IMG_INIT_WEBP)
        TTF_Init()

    def __del__(self):
        TTF_Quit()
        IMG_Quit()

    def Initialize(self) -> None:
        ...

