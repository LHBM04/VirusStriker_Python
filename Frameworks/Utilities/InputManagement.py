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
        self.keyState: dict[int : InputManager.EInputState]    = {}
        self.isPressKey: bool                   = False
        self.mousePosition: Vector2             = Vector2()

    def IsKeyPressed(self):
        self.isPressKey = True

    def SetKeyState(self, key: int, state: EInputState) -> None:
        self.keyState[key] = state

    def GetKeyState(self, key: int) -> EInputState:
        if key not in self.keyState:
            return InputManager.EInputState.NONE

        return self.keyState[key]
    
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

    def Update(self) -> None:
        #print(f"mouse x: {self.mousePosition.x} mouse y: {self.mousePosition.y}")
        for key in self.keyState:
            if key == InputManager.EInputState.DOWN:
                key = InputManager.EInputState.PRESS
                continue
            if key == InputManager.EInputState.UP:
                key = InputManager.EInputState.NONE
                continue