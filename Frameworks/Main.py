import time

from pico2d import *

from Core.System import *
from Core.Sprite import *
from Level.Scene import *
from Utilities.InputSystem import *
from Utilities.AudioSystem import *
from Utilities.FileSystem import *

def HandleEvents(_events: list[Event]) -> None:
    for event in _events:
        if event.type is SDL_QUIT:
            SystemManager().isRunning = False
            return
        if event.type is SDL_KEYDOWN:  # 키가 눌렸을 때
            if event.key is not None:  # event.key가 None이 아닐 때
                InputManager().isKeyPressed = True
                InputManager().SetKeyState(int(event.key), EInputState.DOWN)
            return
        elif event.type is SDL_KEYUP:  # 키가 올라갔을 때
            if event.key is not None:  # event.key가 None이 아닐 때
                InputManager().isKeyPressed = False
                InputManager().SetKeyState(int(event.key), EInputState.UP)
            return

g_previousTime: float       = time.time()   # 이전 시간
g_currentTime: float        = 0.0           # 현재 시간

g_fps: float            = 0.0   # 현재 프레임
g_fpsDeltaTime: float   = 0.0   # 프레임을 계산하기 위한 시간 변화량.

if __name__ == "__main__":
    SystemManager().Inintialize()

    while SystemManager().isRunning:
        HandleEvents(get_events())
        
        if SceneManager().isResetDeltaTime:
            g_previousTime = time.time()

        # Delta Time 계산
        g_currentTime = time.time()
        delteTime = g_currentTime - g_previousTime
        
        # Fixed Delta Time 계산
        fixedUpdateTime = 1.0 / 50.0
        fixedDeltaTime  = delteTime

        if fixedDeltaTime >= 2.0:
            fixedDeltaTime = 2.0

        while fixedDeltaTime > fixedUpdateTime:
            fixedDeltaTime -= fixedUpdateTime
            SystemManager().FixedUpdate(fixedUpdateTime)

        # 초당 프레임 계산
        g_fps += 1
        g_fpsDeltaTime += delteTime
        
        if g_fpsDeltaTime > 1.0:
            SystemManager().gameFPS = g_fps
            g_fps = 0
            g_fpsDeltaTime = 0.0

        SystemManager().Update(delteTime)
        
        g_previousTime = g_currentTime  # 현재 시간으로 prevTime 업데이트
        update_canvas()  # 캔버스 업데이트

    SystemManager().CleanUp()