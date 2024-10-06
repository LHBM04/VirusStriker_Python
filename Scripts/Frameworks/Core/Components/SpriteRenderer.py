from enum import Enum

from pico2d import *

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Color import Color
from Core.Utilities.Mathematics.Vector3 import Vector3

from typing import final

@final
class Color:
    @staticmethod
    def MinValue() -> int:
        return 0

    @staticmethod
    def MaxValue() -> int:
        return 255

    def __init__(self,
                 _r: int = MaxValue(),
                 _g: int = MaxValue(),
                 _b: int = MaxValue(),
                 _a: int = MaxValue()) -> None:
        self.__r: int = max(self.MinValue(), min(_r, self.MaxValue()))
        self.__g: int = max(self.MinValue(), min(_g, self.MaxValue()))
        self.__b: int = max(self.MinValue(), min(_b, self.MaxValue()))
        self.__a: int = max(self.MinValue(), min(_a, self.MaxValue()))

    @property
    def r(self) -> int:
        return self.__r

    @r.setter
    def r(self, _r: int) -> None:
        self.__r = max(self.MinValue(), min(_r, self.MaxValue()))

    @property
    def g(self) -> int:
        return self.__g

    @g.setter
    def g(self, _g: int) -> None:
        self.__g = max(self.MinValue(), min(_g, self.MaxValue()))

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, _b: int) -> None:
        self.__r = max(self.MinValue(), min(_b, self.MaxValue()))

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, _a: int) -> None:
        self.__a = max(self.MinValue(), min(_a, self.MaxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return (self.r == _other.r and
                self.g == _other.g and
                self.b == _other.b and
                self.a == _other.a)

    def __ne__(self, _other: 'Color') -> bool:
        return not self.__eq__(_other)

COLOR_RED: Color        = Color(255, 0, 0)
COLOR_GREEN: Color      = Color(0, 255, 0)
COLOR_BLUE: Color       = Color(0, 0, 255)
COLOR_YELLOW: Color     = Color(255, 255, 0)
COLOR_CYAN: Color       = Color(0, 255, 255)
COLOR_MAGENTA: Color    = Color(255, 0, 255)
COLOR_WHITE: Color      = Color(255, 255, 255)
COLOR_BLACK: Color      = Color(0, 0, 0)
COLOR_GRAY: Color       = Color(128, 128, 128)
COLOR_ORANGE: Color     = Color(255, 165, 0)
COLOR_CLEAR: Color     = Color(0, 0, 0, 0)


# 그려야 할 그래픽들의 우선 순위를 나타내는 열거형. (가장 높은 것이 우선 순위)
class ESortingLayer(Enum):
    NONE        = 0
    BACKGROUND  = 1
    FOREGROUND  = 2
    OBJECT      = 3
    UI          = 4

class SpriteRenderer(Component):
    def __init__(self, _owner: GameObject):
        super().__init__(_owner)

        self.__sprite: Image                = None                                      # 렌더링할 이미지 리소스.
        self.__isFlipX: bool                = False                                     # X축 뒤집기 여부.
        self.__isFlipY: bool                = False                                     # Y축 뒤집기 여부.
        self.__color: Color                 = Color(255, 255, 255, 255)    # 해당 이미지가 그려질 컬러.(RGBA)
        self.__sortingLayer: ESortingLayer  = ESortingLayer.NONE                        # 해당 이미지가 렌더링 우선 순위
        self.__orderInLayer: int            = 0                                         # 해당 이미지가 렌더링 순서

    # [Properties] #
    @property
    def sprite(self) -> Image:
        return self.__sprite

    @sprite.setter
    def sprite(self, _sprite: Image) -> None:
        self.__sprite = _sprite

    @property
    def position(self) -> Vector3:
        return self.gameObject.transform.position

    @position.setter
    def position(self, _position: Vector3) -> None:
        self.gameObject.transform.position = _position

    @property
    def scale(self) -> Vector3:
        return self.gameObject.transform.scale

    @scale.setter
    def scale(self, _scale: Vector3) -> None:
        self.gameObject.transform.scale = _scale

    @property
    def rotation(self) -> Vector3:
        return self.gameObject.transform.rotation

    @rotation.setter
    def rotation(self, _rotation: Vector3) -> None:
        self.gameObject.transform.rotation = _rotation

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, _color: Color) -> None:
        self.__color = _color

    @property
    def sortingLayer(self) -> ESortingLayer:
        return self.__sortingLayer

    @sortingLayer.setter
    def sortingLayer(self, _sortingLayer: ESortingLayer) -> None:
        self.__sortingLayer = _sortingLayer

    @property
    def orderInLayer(self) -> int:
        return self.__orderInLayer

    @orderInLayer.setter
    def orderInLayer(self, _orderInLayer: int) -> None:
        self.__orderInLayer = _orderInLayer

    def Render(self):
        if self.__sprite is None:
            raise ValueError("[Oops!] 렌더링할 Sprite가 존재하지 않습니다.")

        self.__sprite.composite_draw(self.gameObject.transform.rotation.z,
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