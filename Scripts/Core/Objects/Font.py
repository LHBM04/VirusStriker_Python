from typing import final

from sdl2.sdlttf import *

from Core.Objects.Object import Object

@final
class Font(Object):
    def __init__(self, _font: TTF_Font) -> None:
        super().__init__()
        
        self.__font: TTF_Font = _font

    def __del__(self) -> None:
        TTF_CloseFont(self.__font)

    @property
    def font(self) -> TTF_Font:
        return self.__font