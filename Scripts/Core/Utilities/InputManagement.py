from enum import Enum
from typing import final, Dict

from pico2d import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.Mathematics import Vector2

class EInputState(Enum):
    """
    키/마우스 버튼의 상태를 나타내는 열거형.
    """
    NONE = 0
    UP = 1
    DOWN = 2
    PRESS = 3

@final
class InputManager(metaclass=Singleton):
    """
    키보드와 마우스 입력을 관리합니다.
    """
    def __init__(self) -> None:
        self.keyState: Dict[int, EInputState]       = {}
        self.buttonState: Dict[int, EInputState]    = {}
        self.isPressKey: bool                       = False
        self.mousePosition: Vector2                 = Vector2()

    def IsKeyPressed(self) -> None:
        """
        키가 눌린 상태를 표시합니다.
        """
        self.isPressKey = True

    def GetKeyState(self, key: int) -> EInputState:
        """
        주어진 키의 현재 상태를 반환합니다.
        :param key: 상태를 확인할 키의 코드.
        :return: 해당 키의 EInputState 값.
        """
        if key not in self.keyState:
            return EInputState.NONE
        return self.keyState[key]

    def SetKeyState(self, key: int, state: EInputState) -> None:
        """
        주어진 키의 상태를 설정합니다.
        :param key: 상태를 설정할 키의 코드.
        :param state: 설정할 EInputState 값.
        """
        self.keyState[key] = state

    def GetKey(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 눌려 있는지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 눌려 있으면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.keyState:
            return False
        return self.GetKeyState(_keyCode) == EInputState.DOWN

    def GetKeyDown(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 눌린 상태인지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 눌린 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.keyState:
            return False
        return self.GetKeyState(_keyCode) == EInputState.PRESS

    def GetKeyUp(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 떼어진 상태인지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 떼어진 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.keyState:
            return False
        return self.GetKeyState(_keyCode) == EInputState.UP

    def GetMouseButton(self, _buttonCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 눌려 있는지 확인합니다.
        :param _buttonCode: 확인할 버튼의 코드.
        :return: 버튼이 눌려 있으면 True, 그렇지 않으면 False.
        """
        if _buttonCode not in self.keyState:
            return False
        return self.GetMouseButtonState(_buttonCode) == EInputState.DOWN

    def GetMouseButtonDown(self, _keyCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 눌린 상태인지 확인합니다.
        :param _keyCode: 확인할 버튼의 코드입니다.
        :return: 버튼이 눌린 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.keyState:
            return False
        return self.GetMouseButtonState(_keyCode) == EInputState.PRESS

    def GetMouseButtonUp(self, _keyCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 떼어진 상태인지 확인합니다.
        :param _keyCode: 확인할 버튼의 코드.
        :return: 버튼이 떼어진 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.keyState:
            return False
        return self.GetMouseButtonState(_keyCode) == EInputState.UP

    def GetMouseButtonState(self, key: int) -> EInputState:
        """
        주어진 마우스 버튼의 현재 상태를 반환합니다.
        :param key: 상태를 확인할 마우스 버튼의 코드.
        :return: 해당 버튼의 EInputState 값.
        """
        if key not in self.buttonState:
            return EInputState.NONE
        return self.buttonState[key]

    def GetCursorPosition(self) -> Vector2:
        """
        현재 커서 위치를 반환합니다.
        :return: 현재 커서 위치.
        """
        SDL_GetMouseState(self.mousePosition.x, self.mousePosition.y)
        return self.mousePosition

    def SetMouseButtonState(self, _buttonCode: int, state: EInputState) -> None:
        """
        주어진 마우스 버튼의 상태를 설정합니다.
        :param _buttonCode: 상태를 설정할 마우스 버튼의 코드.
        :param state: 설정할 EInputState 값.
        """
        self.buttonState[_buttonCode] = state

    def Update(self) -> None:
        """
        입력 상태를 업데이트합니다.
        """
        for key in self.keyState.keys():
            if self.keyState[key] == EInputState.DOWN:
                self.keyState[key] = EInputState.PRESS
            elif self.keyState[key] == EInputState.UP:
                self.keyState[key] = EInputState.NONE

        for button in self.buttonState.keys():
            if self.buttonState[button] == EInputState.DOWN:
                self.buttonState[button] = EInputState.PRESS
            elif self.buttonState[button] == EInputState.UP:
                self.buttonState[button] = EInputState.NONE
