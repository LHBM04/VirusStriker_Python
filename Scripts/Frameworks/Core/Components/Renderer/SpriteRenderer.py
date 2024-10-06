from pico2d import *

from Core.Components.Component import Component
from Core.Components.Renderer.Color import Color
from Core.Components.Renderer.ESortingLayer import ESortingLayer
from Core.Components.Objects.GameObject import GameObject
from Core.Utilities.Mathematics.Rotation import Rotation
from Core.Utilities.Mathematics.Vector2 import Vector2

# 스프라이트 이미지를 출력하는 컴포넌트.
class SpriteRenderer(Component):
    def __init__(self, _owner: 'GameObject'):
        super().__init__(_owner)

        self.__sprite: Image                  = None
        self.__color: Color                 = Color(255, 255, 255, 255)       # 해당 스프라이트가 그려질 컬러.(RGBA)
        self.__sortingLayer: ESortingLayer  = ESortingLayer.NONE           # 해당 스프라이트의 렌더링 우선 순위
        self.__orderInLayer: int            = 0                                      # 해당 스프라이트의 렌더링 순서

    @property
    def sprite(self) -> Image:
        return self.__sprite

    @sprite.setter
    def sprite(self, _newSpirte: Image) -> None:
        self.__sprite = _newSpirte

    @property
    def position(self) -> Vector2:
        return self.owner.transform.position

    @position.setter
    def position(self, _newPosition: Vector2) -> None:
        self.owner.transform.position = _newPosition

    @property
    def scale(self) -> Vector2:
        return self.owner.transform.scale

    @scale.setter
    def scale(self, _newScale: Vector2) -> None:
        self.owner.transform.scale = _newScale

    @property
    def rotation(self) -> Rotation:
        return self.owner.transform.rotation

    @rotation.setter
    def rotation(self, _newRotation: Rotation) -> None:
        self.owner.transform.rotation = _newRotation

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
    def sortingLayer(self, _newSortingLayer: ESortingLayer) -> None:
        self.__sortingLayer = _newSortingLayer

    @property
    def orderInLayer(self) -> int:
        return self.__orderInLayer

    @orderInLayer.setter
    def orderInLayer(self, _newOrderInLayer: int) -> None:
        self.__orderInLayer = _newOrderInLayer

    def Render(self):
        if self.__sprite is None:
            raise ValueError("[Oops!] 렌더링할 Sprite가 존재하지 않습니다.")

        x: float        = self.owner.transform.position.x
        y: float        = self.owner.transform.position.y
        scaleX: float   = self.owner.transform.scale.x
        scaleY: float   = self.owner.transform.scale.y
        isFilp: str     = (('w' if self.owner.transform.rotation.x else '') +
                           ('h' if self.owner.transform.rotation.y else ''))
        rotate: float   = self.owner.transform.rotation.z

        self.__sprite.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(self.__sprite.texture, int(self.color.r), int(self.color.g), int(self.color.b))
        SDL_SetTextureAlphaMod(self.__sprite.texture, int(self.color.a))
        SDL_SetTextureBlendMode(self.__sprite.texture, SDL_BLENDMODE_BLEND)