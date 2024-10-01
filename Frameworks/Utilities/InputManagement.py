from enum import Enum
from pico2d import *
from Utilities.Singleton import *
from Utilities.Vector2 import *

# 해당 게임의 키 입력을 감시하고 관리하는 매니저.
class InputManager(metaclass = Singleton):
    class EInputState(Enum):
        NONE    = 0
        UP      = 1
        DOWN    = 2
        PRESS   = 3

    def __init__(self) -> None:
        self.keyState: dict[int : InputManager.EInputState]     = {}
        self.buttonState: dict[int : InputManager.EInputState]  = {}
        self.isPressKey: bool                                   = False
        self.mousePosition: Vector2                             = Vector2()

    def IsKeyPressed(self):
        self.isPressKey = True

    def SetKeyState(self, key: int, state: EInputState) -> None:
        self.keyState[key] = state

    def SetMouseState(self, button: int, state: EInputState) -> None:
        self.buttonState[button] = state

    def GetKeyState(self, key: int) -> EInputState:
        if key not in self.keyState:
            return InputManager.EInputState.NONE

        return self.keyState[key]
    
    def GetMouseState(self, key: int) -> EInputState:
        if key not in self.buttonState:
            return InputManager.EInputState.NONE

        return self.buttonState[key]
    
    def GetKey(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == InputManager.EInputState.DOWN
    
    def GetKeyDown(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == InputManager.EInputState.PRESS
    
    def GetKeyUp(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetKeyState(_keyCode) == InputManager.EInputState.UP
    
    def GetButton(self, _buttonCode: int) -> bool:
        if _buttonCode not in self.keyState:
            return False
        
        return self.GetMouseState(_buttonCode) == InputManager.EInputState.DOWN
    
    def GetButtonDown(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetMouseState(_keyCode) == InputManager.EInputState.PRESS
    
    def GetButtonUp(self, _keyCode: int) -> bool:
        if _keyCode not in self.keyState:
            return False
        
        return self.GetMouseState(_keyCode) == InputManager.EInputState.UP
    
    def GetMousePosition(self) -> Vector2:
        SDL_GetMouseState(self.mousePosition.x, self.mousePosition.y)
        return self.mousePosition

    def Update(self) -> None:
        for key in list(self.keyState.keys()):
            if self.keyState[key] == InputManager.EInputState.DOWN:
                self.keyState[key] = InputManager.EInputState.PRESS
            elif self.keyState[key] == InputManager.EInputState.UP:
                self.keyState[key] = InputManager.EInputState.NONE

        for key in list(self.buttonState.keys()):
            if self.buttonState[key] == InputManager.EInputState.DOWN:
                self.buttonState[key] = InputManager.EInputState.PRESS
            elif self.buttonState[key] == InputManager.EInputState.UP:
                self.buttonState[key] = InputManager.EInputState.NONE