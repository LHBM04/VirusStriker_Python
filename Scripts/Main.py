from typing import List

from pico2d import *

from Core.Utilities.InputManagement import EInputState, InputManager
from Core.Utilities.Mathematics import Vector2
from Core.Utilities.SystemManagement import SystemManager

def ReceiveEvent() -> List[Event]:
    """
    이벤트를 받아, 이를 처리한 후 수신합니다.
    :return: 처리한 이벤트.
    """
    gotEvent: SDL_Event = SDL_Event()
    events: List[Event] = []

    # SDL 이벤트 처리 루프
    while SDL_PollEvent(ctypes.byref(gotEvent)):
        event: Event = Event(gotEvent.type)

        # 이벤트 타입 확인 및 관련 정보 저장
        if event.type in {SDL_QUIT,
                          SDL_KEYDOWN,
                          SDL_KEYUP,
                          SDL_MOUSEMOTION,
                          SDL_MOUSEBUTTONDOWN,
                          SDL_MOUSEBUTTONUP}:
            if (event.type in {SDL_KEYDOWN, SDL_KEYUP} and
                not gotEvent.key.repeat):  # 키보드 입력
                event.key = gotEvent.key.keysym.sym

            elif event.type == SDL_MOUSEMOTION:  # 마우스 이동
                event.x, event.y = gotEvent.motion.x, gotEvent.motion.y

            elif event.type in {SDL_MOUSEBUTTONUP, SDL_MOUSEBUTTONDOWN}:  # 마우스 버튼
                event.button, event.x, event.y = gotEvent.button.button, gotEvent.button.x, gotEvent.button.y

            events.append(event)

    return events

def SendEvent(_events: List[Event]) -> None:
    """
    이벤트를 수신하여 처리합니다.
    :param _events: 수신 받은 이벤트.
    """
    for event in _events:
        if event.type == SDL_QUIT:
            SystemManager().Quit()

        elif event.type in {SDL_KEYDOWN,
                            SDL_KEYUP}:
            InputManager().isPressKey = event.type == SDL_KEYDOWN
            state = EInputState.DOWN if event.type == SDL_KEYDOWN else EInputState.UP
            InputManager().SetKeyState(event.key, state)

        elif event.type == SDL_MOUSEMOTION:
            InputManager().mousePosition = Vector2(event.x, event.y)

        elif event.type in {SDL_MOUSEBUTTONDOWN,
                            SDL_MOUSEBUTTONUP}:
            state = EInputState.DOWN if event.type == SDL_MOUSEBUTTONDOWN else EInputState.UP
            InputManager().SetMouseButtonState(event.button, state)
            InputManager().mousePosition = Vector2(event.x, event.y)


if __name__ == "__main__":
    print("Hello, World!")
