import time as Time

from pico2d import *

from Core.System import *
from Level.LevelManagement import *
from Utilities.AudioManagement import *
from Utilities.FileManagement import *
from Utilities.InputManagement import *

def HandleEvents() -> bool:
    events: list[Event] = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            SystemManager().isRunning = False

    return SystemManager().isRunning

if __name__ == "__main__":
    previousTime: float = Time.time()  # 이전 시간
    currentTime: float  = 0.0           # 현재 시간

    fpsDeltaTime: float = 0.0           # 프레임을 계산하기 위한 시간 변화량.

    SystemManager().Inintialize()
    while HandleEvents():
        if LevelManager().isResetDeltaTime:
            previousTime = Time.time()

        # Delta Time 계산
        currentTime = Time.time()
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
        SystemManager().gameFPS += 1
        fpsDeltaTime += deltaTime
        
        if fpsDeltaTime > 1.0:
            SystemManager().gameFPS = 0
            fpsDeltaTime = 0.0

        SystemManager().Update(deltaTime)
        SystemManager().Render()

        # [디버그 코드]
        print(f"Delta Time: {deltaTime}, Fixed Delta Time: {fixedUpdateTime}, FPS: {SystemManager().gameFPS}")
        
        previousTime = currentTime  # 현재 시간으로 prevTime 업데이트
        
    SystemManager().CleanUp()
