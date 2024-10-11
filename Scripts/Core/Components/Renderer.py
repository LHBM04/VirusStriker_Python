from abc import ABCMeta, abstractmethod
from typing import final, Optional

from pico2d import *

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject
from Core.Utilities.Mathematics import Vector2


class Renderer(metaclass = ABCMeta):
    """
    렌더링 작동을 정의합니다.
    """
    @abstractmethod
    def Render(self) -> None:
        """
        렌더링을 진행합니다.
        """
        pass

@final
class SpriteRenderer(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)

        self.__sprite: Optional[Image]  = None
        self.__color: SDL_Color         = SDL_Color(255, 255, 255, 255)
        self.__isFlipX: bool            = False
        self.__isFlipY: bool            = False
        self.__sortingLayer: int        = 0
        self.__orderInLayer: int        = 0

    # region Properties
    @property
    def sprite(self) -> Image:
        return self.__sprite

    @sprite.setter
    def sprite(self, _sprite: Image) -> None:
        self.__sprite = _sprite

    @property
    def position(self) -> Vector2:
        return self.gameObject.transform.position

    @position.setter
    def position(self, _position: Vector2) -> None:
        self.gameObject.transform.position = _position

    @property
    def scale(self) -> Vector2:
        return self.gameObject.transform.scale

    @scale.setter
    def scale(self, _scale: Vector2) -> None:
        self.gameObject.transform.scale = _scale

    @property
    def rotation(self) -> Vector2:
        return self.gameObject.transform.rotation

    @rotation.setter
    def rotation(self, _rotation: Vector2) -> None:
        self.Entity(gameObject).transform.rotation = _rotation

    @property
    def color(self) -> SDL_Color:
        return self.__color

    @color.setter
    def color(self, _color: SDL_Color) -> None:
        self.__color = _color

    @property
    def sortingLayer(self) -> int:
        return self.__sortingLayer

    @sortingLayer.setter
    def sortingLayer(self, _sortingLayer: int) -> None:
        self.__sortingLayer = _sortingLayer

    @property
    def orderInLayer(self) -> int:
        return self.__orderInLayer

    @orderInLayer.setter
    def orderInLayer(self, _orderInLayer: int) -> None:
        self.__orderInLayer = _orderInLayer
    # endregion

    def Render(self):
        if self.__sprite is None:
            raise ValueError("[Oops!] 렌더링할 Sprite가 존재하지 않습니다.")

        self.__sprite.composite_draw(self.gameObject.transform.rotation,
                                     ('w' if self.__isFlipX else '') + ('h' if self.__isFlipY else ''),
                                     self.gameObject.transform.position.x,
                                     self.gameObject.transform.position.y,
                                     self.gameObject.transform.scale.x,
                                     self.gameObject.transform.scale.y)
        SDL_SetTextureColorMod(self.__sprite.texture,
                               int(self.color.r),
                               int(self.color.g),
                               int(self.color.b))
        SDL_SetTextureAlphaMod(self.__sprite.texture,
                               int(self.color.a))
        SDL_SetTextureBlendMode(self.__sprite.texture,
                                SDL_BLENDMODE_BLEND)