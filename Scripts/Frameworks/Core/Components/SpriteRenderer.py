from enum import Enum

from pico2d import *

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics.Vector2 import Vector2

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
    def g(self) -> float:
        return self.__g

    @g.setter
    def g(self, _g: int) -> None:
        self.__g = max(self.MinValue(), min(_g, self.MaxValue()))

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, _b: int) -> None:
        self.__r = max(self.MinValue(), min(_b, self.MaxValue()))

    @property
    def a(self) -> float:
        return self.a

    @a.setter
    def a(self, _a: int) -> None:
        self.a = max(self.MinValue(), min(_a, self.MaxValue()))

    def __eq__(self, _other: 'Color') -> bool:
        return self.__r == _other.__r and self.__g == _other.__g and self.__b == _other.__b and self.a == _other.a

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


# 그려야 할 그래픽들의 우선 순위를 나타내는 열거형. (가장 높은 것이 우선 순위)
class ESortingLayer(Enum):
    NONE        = 0
    BACKGROUND  = 1
    FOREGROUND  = 2
    OBJECT      = 3
    UI          = 4

# 스프라이트 이미지를 출력하는 컴포넌트.
class SpriteRenderer(Component):
    def __init__(self, _owner: 'GameObject'):
        super().__init__(_owner)

        self.sprite: Image = None
        
        self.position: Vector2 = _owner.transform.position            # 해당 스프라이트가 그려질 위치.
        self.scale: Vector2 = _owner.transform.position               # 해당 스프라이트가 그려질 크기
        self.rotation: (bool, bool, float) = _owner.transform.rotation  # 해당 스프라이트가 그려질 회전값.
        
        self.color: Color = Color(255, 255, 255, 255)       # 해당 스프라이트가 그려질 컬러.(RGBA)
        
        self.sortingLayer: ESortingLayer = ESortingLayer.NONE           # 해당 스프라이트의 렌더링 우선 순위
        self.orderInLayer: int = 0                                      # 해당 스프라이트의 렌더링 순서

    def Render(self):
        x: float = self.owner.transform.position.x
        y: float = self.owner.transform.position.y
        scaleX: float = self.owner.transform.scale.x
        scaleY: float = self.owner.transform.scale.y
        rotate: float = self.owner.transform.rotation.z
        isFilp: str = (('w' if self.owner.transform.rotation.x else '') +
                       ('h' if self.owner.transform.rotation.y else ''))

        self.sprite.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(self.sprite.texture, int(self.color.r), int(self.color.g), int(self.color.b))
        SDL_SetTextureAlphaMod(self.sprite.texture, int(self.color.a))
        SDL_SetTextureBlendMode(self.sprite.texture, SDL_BLENDMODE_BLEND)