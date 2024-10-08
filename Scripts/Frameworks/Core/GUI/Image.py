from pico2d import Image

from Core.Components.GameObject import GameObject
from Core.Components.Renderer import Renderer
from Core.Utilities.Mathematics import Vector2
from Core.Utilities.Color import Color

class Image(Renderer):
    def __init__(self, _owner: GameObject, _image: Image = None):
        super().__init__(_owner)

        self.__image: Image                         = _image
        self.__color: Color                         = Color()
        self.__isFlipX: bool                        = False
        self.__isFlipY: bool                        = False
        self.__sortingLayer: Renderer.ESortingLayer = Renderer.ESortingLayer.NONE
        self.__orderInLayer: int                    = 0

    #region [Properties]
    @property
    def image(self) -> Image:
        return self.__image

    @image.setter
    def image(self, _sprite: Image) -> None:
        self.__image = _sprite

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
        self.gameObject.transform.rotation = _rotation

    @property
    def color(self) -> Renderer.Color:
        return self.__color

    @color.setter
    def color(self, _color: Renderer.Color) -> None:
        self.__color = _color

    @property
    def sortingLayer(self) -> Renderer.ESortingLayer:
        return self.__sortingLayer

    @sortingLayer.setter
    def sortingLayer(self, _sortingLayer: Renderer.ESortingLayer) -> None:
        self.__sortingLayer = _sortingLayer

    @property
    def orderInLayer(self) -> int:
        return self.__orderInLayer

    @orderInLayer.setter
    def orderInLayer(self, _orderInLayer: int) -> None:
        self.__orderInLayer = _orderInLayer
    # endregion