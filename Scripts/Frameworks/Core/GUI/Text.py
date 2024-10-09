from pico2d import Font

from Core.Components.GameObject import GameObject
from Core.GUI.UIBehaivor import UIBehavior
from Core.Utilities.Color import Color

class Text(UIBehavior):
    def __init__(self, _owner: GameObject, _font: Font = None):
        super().__init__(_owner)

        self.__font: Font               = _font
        self.__text: str                = ""
        self.__color: Color             = Color(255, 255, 255, 255)

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
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, _color: Color) -> None:
        self.__color = _color
    #endregion
    #region [Methods Override]
    def Render(self):
        super().Render()
        
        if self.__font is None:
            raise ValueError("[Oops!] 해당 인스턴스의 Font가 지정되지 않았습니다.")

        self.__font.draw(self.gameObject.transform.position.x,
                         self.gameObject.transform.position.y,
                         self.__text,
                         (self.__color.r, self.__color.g, self.__color.b))

    def RenderDebug(self):
        super().RenderDebug()
    #endregion