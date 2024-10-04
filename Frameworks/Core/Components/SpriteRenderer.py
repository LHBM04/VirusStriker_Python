from enum import Enum

# 그려야 할 그래픽들의 우선 순위를 나타내는 열거형. (가장 높은 것이 우선 순위)
class ESortingLayer(Enum):
    NONE = 0
    BACKGROUND = 1
    FOREGROUND = 2
    OBJECT = 3
    UI = 4

from pico2d import *

from Frameworks.Core.Components.GameObject import GameObject
from Frameworks.Core.Utilities.Color import Color
from Frameworks.Core.Utilities.Mathematics import Vector2
from Frameworks.Core.Components.Component import Component

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
        rotate: float = self.owner.transform.rotation[2]
        isFilp: str = (('w' if self.owner.transform.rotation[0] else '') +
                       ('h' if self.owner.transform.rotation[1] else ''))

        if (self.color.r > Color.MaxValue() or self.color.g > Color.MaxValue() or
            self.color.b > Color.MaxValue() or self.color.a > Color.MaxValue()):
            raise ValueError("[Oops!] 해당 렌더러의 컬러값이 잘못되었습니다.")

        self.sprite.composite_draw(rotate, isFilp, x, y, scaleX, scaleY)
        SDL_SetTextureColorMod(self.textures.texture, int(self.color.r), int(self.color.g), int(self.color.b))
        SDL_SetTextureAlphaMod(self.textures.texture, int(self.color.a))
        SDL_SetTextureBlendMode(self.textures.texture, SDL_BLENDMODE_BLEND)