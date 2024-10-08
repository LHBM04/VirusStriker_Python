from pico2d import Font

from Core.Components.GameObject import GameObject
from Core.Components.Renderer import Renderer

class TextRenderer(Renderer):
    def __init__(self, _owner: GameObject, _font: Font = None):
        super().__init__(_owner)

        self.__font: Font               = _font
        self.__text: str                = ""
        self.__color: Renderer.Color    = Renderer.Color(255, 255, 255, 255)

    #region [Properties]
    @property
    def font(self) -> Font:
        return self.__font

    @font.setter
    def font(self, _font: Font) -> None:
        self.__font = _font

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, _text: str) -> None:
        self.__text = _text

    @property
    def color(self) -> Renderer.Color:
        return self.__color

    @color.setter
    def color(self, _color: Renderer.Color) -> None:
        self.__color = _color
    #endregion
    #region [Methods Override]
    def Render(self):
        if self.__font is None:
            return

        self.__font.draw(self.gameObject.transform.x,
                         self.gameObject.transform.y,
                         self.__text,
                         self.__color)

    def RenderDebug(self):
        pass
    #endregion