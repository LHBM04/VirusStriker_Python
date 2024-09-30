from enum import Enum
from pico2d import *
from Utilities.Singleton import *

class EInputState(Enum):
    NONE    = 0
    UP      = 1
    DOWN    = 2
    PRESS   = 3

# 해당 게임의 키 입력을 감시하고 관리하는 매니저.
class InputManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.keyState: list[EInputState]    = [None] * 256
        self.isPressKey: bool               = False

    def IsKeyPressed(self):
        self.isPressKey = True

    def SetKeyState(self, key: int, state: EInputState) -> None:
        self.keyState[key] = state

    def GetKeyState(self, key: int) -> EInputState:
        return self.keyState[key]

    def Update(self) -> None:
        for index in range(256):
            if self.keyState[index] == EInputState.DOWN:
                self.keyState[index] = EInputState.PRESS
            elif self.keyState[index] == EInputState.UP:
                self.keyState[index] = EInputState.NONE