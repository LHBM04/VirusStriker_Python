import time as Timer

from pico2d import *

from Core.System import *
from Core.Sprite import *
from Level.LevelManagement import *
from Utilities.AudioManagement import *
from Utilities.FileManagement import *
from Utilities.InputManagement import *

def HandleEvents(_events: list[Event]) -> None:
    for event in _events:
        if event.type == SDL_QUIT:
            SystemManager().isRunning = False
            return
        if event.type == SDL_KEYDOWN:
            if event.key is not None:
                InputManager().isKeyPressed = True
                InputManager().SetKeyState(int(event.key), EInputState.DOWN)
            return
        elif event.type == SDL_KEYUP:
            if event.key is not None:
                InputManager().isKeyPressed = False
                InputManager().SetKeyState(int(event.key), EInputState.UP)
            return

if __name__ == "__main__":
    previousTime: float = Timer.time()   # 이전 시간
    currentTime: float = 0.0             # 현재 시간

    fps: float = 0.0                      # 현재 프레임
    fpsDeltaTime: float = 0.0             # 프레임을 계산하기 위한 시간 변화량.

    SystemManager().Inintialize()

    while SystemManager().isRunning:
        HandleEvents(get_events())
        if LevelManager().isResetDeltaTime:
            previousTime = Timer.time()

        # Delta Time 계산
        currentTime = Timer.time()
        deltaTime = currentTime - previousTime
        
        # Fixed Delta Time 계산
        fixedUpdateTime = 1.0 / 50.0
        fixedDeltaTime = deltaTime

        if fixedDeltaTime >= 2.0:
            fixedDeltaTime = 2.0

        while fixedDeltaTime > fixedUpdateTime:
            fixedDeltaTime -= fixedUpdateTime
            SystemManager().FixedUpdate(fixedUpdateTime)

        # 초당 프레임 계산
        fps += 1
        fpsDeltaTime += deltaTime
        
        if fpsDeltaTime > 1.0:
            SystemManager().gameFPS = fps
            fps = 0
            fpsDeltaTime = 0.0

        clear_canvas()

        SystemManager().Update(deltaTime)
        SystemManager().Render()

        # [디버그 코드]
        #print(f"Delta Time: {deltaTime}, Fixed Delta Time: {fixedDeltaTime}, FPS: {fps}")
        
        previousTime = currentTime  # 현재 시간으로 prevTime 업데이트
        
        update_canvas()  # 캔버스 업데이트

    SystemManager().CleanUp()
