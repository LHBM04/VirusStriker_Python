from argparse import ArgumentError
from socket import send_fds
from tkinter import Image

from multipledispatch import dispatch

from Frameworks.Core.Sprite import Sprite

class Animation:
    def __init__(self, _sprite: list[Sprite]) -> None:
        if _sprite is None or len(_sprite) <= 0:
            raise ArgumentError

        self.sprites: list[Sprite]      = _sprite               # 해당 스프라이트의 텍스쳐들
        self.size: int                  = len(self.sprites)     # 해당 스프라이트의 텍스쳐 개수.
        self.currentSpriteIndex: int    = 0                     # 해당 스프라이트의 현재 텍스쳐 인덱스.

        self.isLoop: bool                   = True              # 해당 스프라이트의 루프 여부.
        self.isEnd: bool                    = False             # 해당 스프라이트의 루프 종료 여부.
        self.currentAnimateTime: float      = 0.1               # 해당 스프라이트의 애니메이션 시간.
        self.animateDeltaTime: float        = 0.0               # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.

    def Update(self, _deltaTime: float):
        self.animateDeltaTime = self.animateDeltaTime + _deltaTime

        if self.animateDeltaTime > self.currentAnimateTime:
            self.animateDeltaTime = self.animateDeltaTime - self.currentAnimateTime
            self.currentSpriteIndex = self.currentSpriteIndex + 1

            if self.currentSpriteIndex >= self.size:
                if self.isLoop:
                    self.currentSpriteIndex = 0
                else:
                    self.currentSpriteIndex = self.currentSpriteIndex - 1
                    self.isEnd = True

    def Render(self):
        if self.currentSpriteIndex >= self.size:
            return

        self.sprites[self.currentSpriteIndex].Render()

class Animator:
    @dispatch(Animation)
    def __init__(self):
        self.animations: dict[str:Animation]    = {}    # 관리할 애니메이션들
        self.currentAnimation: Animation        = None  # 현재 재생 중인 애니메이션

    def AddAnimation(self, _key: str, _animation: Animation):
        self.animations[_key] = _animation

    def SetState(self, _state: str):
        self.currentAnimation = self.animations[_state]

    def Update(self, _deltaTime: float):
        if self.currentAnimation is None:
            return

        self.currentAnimation.Update(_deltaTime)

    def Render(self):
        if self.currentAnimation is None:
            return

        self.currentAnimation.Render()