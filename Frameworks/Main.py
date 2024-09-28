from pico2d import *
import time

g_isRunning: bool = True              # 프로그램 구동 여부.
g_windowName: str = b"Virus Striker" # 프로그램(윈도우) 이름.
g_windowWidth: int = 500             # 가로 해상도 (테스트).
g_windowHeight: int = 800            # 세로 해상도 (테스트).

def HandleEvent() -> None:
    global g_isRunning
    
    # 테스트 구문
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            g_isRunning = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            g_isRunning = False

g_prevTime:float    = 0.0 # 이전 시간
g_curTime:float     = 0.0 # 현재 시간

g_fps:float         = 0.0 # 현재 프레임
g_fpsDeltaTime      = 0.0

def Main() -> None:
    global g_windowWidth
    global g_windowHeight

    open_canvas(g_windowWidth, g_windowHeight) # 캔버스 열기    

    global g_isRunning
    global g_prevTime
    
    g_prevTime = time.time() 
    while g_isRunning:
        HandleEvent()

        global g_curTime

        # Delta Time 계산
        g_curTime = time.time()
        deltaTime = g_curTime - g_prevTime

        # Fixed Delta Time 계산
        fixedUpdateTime = 1.0 / 50.0
        fixedDeltaTime  = deltaTime

        if fixedDeltaTime >= 2.0:
            fixedDeltaTime = 2.0

        while fixedDeltaTime > fixedUpdateTime:
            fixedDeltaTime -= fixedUpdateTime
            # TODO: FixedUpdate() 넣기
            # ex) Core.GetInstance().FixedUpdate(fixedUpdateTime)

        global g_fps
        global g_fpsDeltaTime

        # 초당 프레임 계산
        g_fps += 1
        g_fpsDeltaTime += deltaTime
        
        if g_fpsDeltaTime > 1.0:
            print(f"FPS: {g_fps}")  # FPS 출력
            g_fps = 0
            g_fpsDeltaTime = 0.0

        # TODO: Update() 코드 넣기
        # ex) Core.GetInstance().Update(deltaTime)

        # TODO: Key State 업데이트 해주기
        # ex) InputManager.GetInstance().UpdateKeyStates()
        
        g_prevTime = g_curTime  # 현재 시간으로 prevTime 업데이트
        update_canvas()  # 캔버스 업데이트

    clear_canvas()
    close_canvas()

if __name__ == "__main__":
    Main()