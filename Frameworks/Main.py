import time as Time

from pico2d import *

from Core.System import SystemManager
from Core.Utilities.InputManagement import EInputState, InputManager
from Core.Utilities.Mathematics import Vector2
from Level.SceneManagement import SceneManager

# 이벤트를 받아, 이를 처리한 후 수신합니다.
def ReceiveEvent() -> list[Event]:
    gotEvent: SDL_Event = SDL_Event()
    events: list[Event] = []

    while SDL_PollEvent(ctypes.byref(gotEvent)):
        event = Event(gotEvent.type)
        if event.type in (SDL_QUIT, SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP):
            if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:                                            # 키보드 입력
                if not gotEvent.key.repeat:
                    event.key = gotEvent.key.keysym.sym
            elif event.type == SDL_MOUSEMOTION:                                                                 # 마우스 조작
                event.x, event.y = gotEvent.motion.x, gotEvent.motion.y
            elif event.type == SDL_MOUSEBUTTONUP or event.type == SDL_MOUSEBUTTONDOWN:                          # 마우스 클릭
                event.button, event.x, event.y = gotEvent.button.button, gotEvent.button.x, gotEvent.button.y
            
            events.append(event)

    return events

# 수신한 이벤트를 받아 처리합니다.
def SendEvent(_events: list[Event]) -> None:
    for event in _events:
        if event.type == SDL_QUIT:
            SystemManager().isRunning = False
        elif event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
            if event.type == SDL_KEYDOWN:
                InputManager().isPressKey = True
                InputManager().SetKeyState(event.key, EInputState.DOWN)
            elif event.type == SDL_KEYUP:
                InputManager().isPressKey = False
                InputManager().SetKeyState(event.key, EInputState.UP)
        elif event.type == SDL_MOUSEMOTION:
                InputManager().mousePosition = Vector2(event.x, event.y)
        elif event.type == SDL_MOUSEBUTTONUP or event.type == SDL_MOUSEBUTTONDOWN:      
                InputManager().isPressKey = True
                InputManager().SetMouseState(event.key, EInputState.DOWN)
                InputManager().mousePosition = Vector2(event.x, event.y)

if __name__ == "__main__":
    previousTime: float = Time.time()   # 이전 프레임 시간
    currentTime: float  = 0.0           # 현재 프레임 시간

    fixedDeltaTime: float = 0.0         # 고정 시간 변화량
    fixedUpdateTime: float = 1.0 / 5.0  # 고정된 시간 주기 (1/50.0 sec 고정)

    fpsDeltaTime: float = 0.0           # 프레임을 계산하기 위한 시간 변화량.

    SystemManager().Inintialize()
    while SystemManager().isRunning:
        SendEvent(ReceiveEvent())

        if SceneManager().isResetDeltaTime: # Scene이 전환된다면 이전 프레임을 다시 초기화
            previousTime = Time.time()
        
        # Delta Time 계산 구문
        currentTime = Time.time()
        deltaTime = currentTime - previousTime
        
        # Fixed Delta Time 계산 구문
        fixedUpdateTime = 1.0 / 50.0    # 시간 주기를 고정
        fixedDeltaTime = 0.0            # 0.0으로 초기화
        fixedDeltaTime += deltaTime

        if fixedDeltaTime >= 2.0:       # 2.0초를 넘어가면 2.0초로 고정.
            fixedDeltaTime = 2.0

        while fixedDeltaTime > fixedUpdateTime:
            fixedDeltaTime -= fixedUpdateTime
            SystemManager().FixedUpdate(fixedUpdateTime)

        # 초당 프레임 계산 구문
        SystemManager().gameFPS += 1
        fpsDeltaTime += deltaTime
        
        if fpsDeltaTime > 1.0:  
            SystemManager().gameFPS = 0
            fpsDeltaTime = 0.0

        SystemManager().Update(deltaTime)
        SystemManager().Render()

        previousTime = currentTime  # 이전 프레임 경과 시간을 현재 프레임 경과 시간으로 교체.
        
    SystemManager().CleanUp()
