from enum import Enum
from typing import final, Dict, Any

from sdl2 import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.Mathematics import Vector2

@final
class Input:
    class EState(Enum):
        NONE    = 0,
        UP      = 1,
        DOWN    = 2,
        PRESS   = 3

    class EType(Enum):
        NONE    = 0,
        UP      = 1,
        DOWN    = 2,
        LEFT    = 3,
        RIGHT   = 4,
        OK      = 5,
        NO      = 6,
        SHOOT   = 7,
        BOMB    = 8,
        SWITCH  = 9,
        ENTER   = 10,
        ESCAPE  = 11,

    def __init__(self, _value: int, _type: EType) -> None:
        self.__value: int           = _value
        self.__type: Input.EType    = Input.EType.NONE
        self.__state: Input.EState  = Input.EState.NONE

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, _value: int) -> None:
        self.__value = _value

    @property
    def type(self) -> EType:
        return self.__type

    @type.setter
    def type(self, _value: EType) -> None:
        self.__type = _value

    @property
    def state(self) -> EState:
        return self.__state

    @state.setter
    def state(self, _value: EState) -> None:
        self.__state = _value

@final
class InputManager(metaclass = Singleton):
    """
    키보드와 마우스 입력을 관리합니다.
    """
    class EState(Enum):
        """
        키/마우스 버튼의 상태를 나타내는 열거형.
        """
        NONE    = 0 # 무상태.
        UP      = 1 # 키 올라감.
        DOWN    = 2 # 키 눌려짐.
        PRESS   = 3 # 키 눌림.

    def __init__(self) -> None:
        self.__keyState: Dict[int, InputManager.EState]       = {}
        self.__buttonState: Dict[int, InputManager.EState]    = {}
        self.__isKeyPressed: bool                       = False
        self.__mousePosition: Vector2                 = Vector2()

    def __del__(self):
        ...

    def ProceedInput(self, _event: SDL_Event) -> None:
        if _event.type in { SDL_KEYUP, SDL_KEYDOWN }:
            self.__keyState[_event.key.keysym.sym] = InputManager.EState.DOWN if _event.type == SDL_KEYDOWN else InputManager.EState.UP

        elif _event.type in { SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP }:
            self.__buttonState[_event.button.button] = InputManager.EState.DOWN if _event.type == SDL_MOUSEBUTTONDOWN else InputManager.EState.UP
            self.__mousePosition = Vector2(_event.button.x, _event.button.y)

        elif _event.type == SDL_MOUSEMOTION:
            self.__mousePosition = Vector2(_event.button.x, _event.button.y)

    @property
    def isKeyPressed(self) -> bool:
        """
        키가 눌린 상태를 표시합니다.
        """
        return self.__isKeyPressed

    def GetKeyState(self, key: int) -> EState:
        """
        주어진 키의 현재 상태를 반환합니다.
        :param key: 상태를 확인할 키의 코드.
        :return: 해당 키의 EInputState 값.
        """
        if key not in self.__keyState:
            return InputManager.EState.NONE
        return self.__keyState[key]

    def GetKey(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 눌려 있는지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 눌려 있으면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.__keyState:
            return False
        return self.GetKeyState(_keyCode) == InputManager.EState.DOWN

    def GetKeyDown(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 눌린 상태인지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 눌린 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.__keyState:
            return False
        return self.GetKeyState(_keyCode) == InputManager.EState.PRESS

    def GetKeyUp(self, _keyCode: int) -> bool:
        """
        주어진 키가 현재 떼어진 상태인지 확인합니다.
        :param _keyCode: 확인할 키의 코드.
        :return: 키가 떼어진 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.__keyState:
            return False
        return self.GetKeyState(_keyCode) == InputManager.EState.UP

    def GetMouseButton(self, _buttonCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 눌려 있는지 확인합니다.
        :param _buttonCode: 확인할 버튼의 코드.
        :return: 버튼이 눌려 있으면 True, 그렇지 않으면 False.
        """
        if _buttonCode not in self.__keyState:
            return False
        return self.GetMouseButtonState(_buttonCode) == InputManager.EState.DOWN

    def GetMouseButtonDown(self, _keyCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 눌린 상태인지 확인합니다.
        :param _keyCode: 확인할 버튼의 코드입니다.
        :return: 버튼이 눌린 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.__keyState:
            return False
        return self.GetMouseButtonState(_keyCode) == InputManager.EState.PRESS

    def GetMouseButtonUp(self, _keyCode: int) -> bool:
        """
        주어진 마우스 버튼이 현재 떼어진 상태인지 확인합니다.
        :param _keyCode: 확인할 버튼의 코드.
        :return: 버튼이 떼어진 상태면 True, 그렇지 않으면 False.
        """
        if _keyCode not in self.__keyState:
            return False
        return self.GetMouseButtonState(_keyCode) == InputManager.EState.UP

    def GetMouseButtonState(self, key: int) -> EState:
        """
        주어진 마우스 버튼의 현재 상태를 반환합니다.
        :param key: 상태를 확인할 마우스 버튼의 코드.
        :return: 해당 버튼의 EInputState 값.
        """
        if key not in self.__buttonState:
            return InputManager.EState.NONE
        return self.__buttonState[key]

    def GetCursorPosition(self) -> Vector2:
        """
        현재 커서 위치를 반환합니다.
        :return: 현재 커서 위치.
        """
        SDL_GetMouseState(self.__mousePosition.x, self.__mousePosition.y)
        return self.__mousePosition

    def Update(self) -> None:
        """
        입력 상태를 업데이트합니다.
        """
        if self.__keyState:
            for key in self.__keyState.keys():
                if self.__keyState[key] == InputManager.EState.DOWN:
                    self.__keyState[key] = InputManager.EState.PRESS
                elif self.__keyState[key] == InputManager.EState.UP:
                    self.__keyState[key] = InputManager.EState.NONE

        if self.__buttonState:
            for button in self.__buttonState.keys():
                if self.__buttonState[button] == InputManager.EState.DOWN:
                    self.__buttonState[button] = InputManager.EState.PRESS
                elif self.__buttonState[button] == InputManager.EState.UP:
                    self.__buttonState[button] = InputManager.EState.NONE
