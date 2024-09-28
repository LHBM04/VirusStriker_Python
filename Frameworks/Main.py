from pico2d import *
from pydub import AudioSegment
from pydub.playback import play
import time
from Core.Core import *
from Utilities.Resource import *
from Utilities.AudioSystem import *

g_window_name: str   = "Virus Striker"   # 프로그램(윈도우) 이름.
g_window_width: int  = 1280              # 가로 해상도 (테스트).
g_window_height: int = 800               # 세로 해상도 (테스트).
g_is_running: bool   = True              # 프로그램 구동 여부.

def handle_event() -> None:
    global g_is_running
    
    # 테스트 구문
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            g_is_running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            g_is_running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            play_jingle_bgm(test_bgm_3)

g_previous_time: float       = 0.0 # 이전 시간
g_current_time: float        = 0.0 # 현재 시간

g_fps: float            = 0.0 # 현재 프레임
g_fps_delta_time: float   = 0.0

def main() -> None:
    global g_window_width
    global g_window_height

    open_canvas(g_window_width, g_window_height) # 캔버스 열기

    play_primary_bgm(test_bgm_1)

    global g_is_running
    global g_previous_time
    
    g_previous_time = time.time()
    while g_is_running:
        handle_event()
        update_bgm_state()

        # Delta Time 계산
        global g_current_time

        g_current_time = time.time()
        delta_time = g_current_time - g_previous_time

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
        global g_fps_delta_time

        # 초당 프레임 계산
        g_fps += 1
        g_fps_delta_time += delta_time
        
        if g_fps_delta_time > 1.0:
            print(f"FPS: {g_fps}")  # FPS 출력
            g_fps = 0
            g_fps_delta_time = 0.0

        # TODO: Update() 코드 넣기
        # ex) Core.GetInstance().Update(delta_time)

        # TODO: Key State 업데이트 해주기
        # ex) InputManager.GetInstance().UpdateKeyStates()
        
        g_previous_time = g_current_time  # 현재 시간으로 prevTime 업데이트
        update_canvas()  # 캔버스 업데이트

    clear_canvas()
    close_canvas()

if __name__ == "__main__":
    main()