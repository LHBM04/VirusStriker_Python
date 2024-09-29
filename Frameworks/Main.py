from pico2d import *
import time
from Core.Sprite import *
from Utilities.AudioSystem import *
from Utilities.FileSystem import *

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

g_testSprite = Sprite("Resources/Sprites/Objects/Actors/Player/Idle")

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

        clear_canvas()
       
        # Delta Time 계산
        global g_currentTime

        g_currentTime = time.time()
        delteTime = g_currentTime - g_previousTime
        
        global g_testSprite
        g_testSprite.Update(delteTime)
        g_testSprite.Render()
        
        # Fixed Delta Time 계산
        fixedUpdateTime = 1.0 / 50.0
        fixedDeltaTime  = delteTime

        if fixedDeltaTime >= 2.0:
            fixedDeltaTime = 2.0

        while fixedDeltaTime > fixedUpdateTime:
            fixedDeltaTime -= fixedUpdateTime
            # TODO: FixedUpdate() 넣기
            # ex) Core.GetInstance().FixedUpdate(fixed_update_time)

        global g_fps
        global g_fpsDeltaTime

        # 초당 프레임 계산
        g_fps += 1
        g_fpsDeltaTime += delteTime
        
        if g_fpsDeltaTime > 1.0:
            # print(f"FPS: {g_fps}")  # FPS 출력
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