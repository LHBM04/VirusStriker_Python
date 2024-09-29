from pico2d import *
import time
from Core.Core import *
from Utilities.AudioSystem import *

g_windowName: str   = "Virus Striker"   # 프로그램(윈도우) 이름.
g_windowWidth: int  = 1280              # 가로 해상도 (테스트).
g_windowHeight: int = 800               # 세로 해상도 (테스트).
g_isRunning: bool   = True              # 프로그램 구동 여부.

def HandleEvent() -> None:
    global g_isRunning
    
    # 테스트 구문
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            g_isRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            g_isRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            PlayJingle(testBGM3)

g_previousTime: float       = 0.0 # 이전 시간
g_currentTime: float        = 0.0 # 현재 시간

g_fps: float            = 0.0 # 현재 프레임
g_fpsDeltaTime: float   = 0.0

def main() -> None:
    global g_windowWidth
    global g_windowHeight

    open_canvas(g_windowWidth, g_windowHeight) # 캔버스 열기

    PlayPrimaryBGM(testBGM1)

    global g_isRunning
    global g_previousTime
    
    g_previousTime = time.time()
    while g_isRunning:
        HandleEvent()
        UpdateBGMState()

        # Delta Time 계산
        global g_currentTime

        g_currentTime = time.time()
        delta_time = g_currentTime - g_previousTime

        # Fixed Delta Time 계산
        fixed_update_time = 1.0 / 50.0
        fixed_delta_time  = delta_time

        if fixed_delta_time >= 2.0:
            fixed_delta_time = 2.0

        while fixed_delta_time > fixed_update_time:
            fixed_delta_time -= fixed_update_time
            # TODO: FixedUpdate() 넣기
            # ex) Core.GetInstance().FixedUpdate(fixed_update_time)

        global g_fps
        global g_fpsDeltaTime

        # 초당 프레임 계산
        g_fps += 1
        g_fpsDeltaTime += delta_time
        
        if g_fpsDeltaTime > 1.0:
            print(f"FPS: {g_fps}")  # FPS 출력
            g_fps = 0
            g_fpsDeltaTime = 0.0

        # TODO: Update() 코드 넣기
        # ex) Core.GetInstance().Update(delta_time)

        # TODO: Key State 업데이트 해주기
        # ex) InputManager.GetInstance().UpdateKeyStates()
        
        g_previousTime = g_currentTime  # 현재 시간으로 prevTime 업데이트
        update_canvas()  # 캔버스 업데이트

    clear_canvas()
    close_canvas()

if __name__ == "__main__":
    main()