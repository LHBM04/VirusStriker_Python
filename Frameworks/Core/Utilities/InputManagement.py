from enum import Enum
from typing import final

from pico2d import *

from Frameworks.Core.Utilities.Singleton import Singleton
from Frameworks.Core.Utilities.Mathematics import Vector2

class EInputState(Enum):
    NONE    = 0
    UP      = 1
    DOWN    = 2
    PRESS   = 3

# 해당 게임의 키 입력을 감시하고 관리하는 매니저.
@final
class InputManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.keyState: dict[int : EInputState]      = {}
        self.buttonState: dict[int : EInputState]   = {}
        self.isPressKey: bool                       = False
        self.mousePosition: Vector2                 = Vector2()

    def IsKeyPressed(self) -> None:
        self.isPressKey = True

    def GetKeyState(self, key: int) -> EInputState:
        if key not in self.keyState:
            return EInputState.NONE

        return self.keyState[key]

    def SetKeyState(self, key: int, state: EInputState) -> None:
        self.keyState[key] = state

    def GetKey(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == EInputState.DOWN

    def GetKeyDown(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == EInputState.PRESS

    def GetKeyUp(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == EInputState.UP

    def GetButton(self, _buttonCode: int) -> bool:
        if _buttonCode not in self.keyState:
            return False
        
        return self.GetMouseState(_buttonCode) == EInputState.DOWN

    def GetButtonDown(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetMouseState(_keyCode) == EInputState.PRESS

    def GetButtonUp(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetMouseState(_keyCode) == EInputState.UP

    def GetMouseState(self, key: int) -> EInputState:
        if key not in self.buttonState:
            return EInputState.NONE

        return self.buttonState[key]

    def GetMousePosition(self) -> Vector2:
        SDL_GetMouseState(self.mousePosition.x, self.mousePosition.y)
        return self.mousePosition

    def SetMouseState(self, button: int, state: EInputState) -> None:
        self.buttonState[button] = state

    def Update(self) -> None:
        for key in list(self.keyState.keys()):
            if self.keyState[key] == EInputState.DOWN:
                self.keyState[key] = EInputState.PRESS
            elif self.keyState[key] == EInputState.UP:
                self.keyState[key] = EInputState.NONE

        for button in list(self.buttonState.keys()):
            if self.buttonState[button] == EInputState.DOWN:
                self.buttonState[button] = EInputState.PRESS
            elif self.buttonState[button] == EInputState.UP:
                self.buttonState[button] = EInputState.NONE