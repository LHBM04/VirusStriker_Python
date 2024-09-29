# TODO: AudioSystem 개발 과정
# 1. 메인 BGM 재생/정지 함수 만들기 (완료)
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 2. 서브 BGM 재생/정지 함수 작성하기 (완료)
# 3. 징글 BGM 재생/정지 함수 작성하기 (완료)
# 4. SFX 재생 로직 작성하기 
#   - 재생 위치 다르게 하기
#   - 오브젝트 풀링 이용해서 SFX 재생 소스 할당하기
import pygame
from enum import Enum

pygame.mixer.init() # pygame.mixer 초기화.

# 재생 중인 BGM의 타입을 나타내는 열거형.
class EBGMState(Enum):
    NONE        = 0
    PRIMARY     = 1
    SECONDARY   = 2
    JINGLE      = 3

current_bgm_type: EBGMState     = EBGMState.NONE    # 현재 재생 중인 BGM의 타입.
previous_bgm_type: EBGMState    = EBGMState.NONE    # 이전에 재생 중이었던 BGM의 타입.

primary_channel: pygame.mixer.Channel   = pygame.mixer.Channel(0)   # 메인 BGM의 재생 채널
secondary_channel: pygame.mixer.Channel = pygame.mixer.Channel(1)   # 서브 BGM의 재생 채널
jingle_channel: pygame.mixer.Channel    = pygame.mixer.Channel(2)   # 징글 BGM의 재생 채널

def play_primary_bgm(_bgm: pygame.mixer.Sound, _is_loop: bool = True, _fade_ms: int = 0):
    global primary_channel
   
    global current_bgm_type
    global previous_bgm_type
 
    current_bgm_type, previous_bgm_type = EBGMState.PRIMARY, current_bgm_type 

    primary_channel.play(_bgm, -1 if _is_loop is True else 0, 0, _fade_ms)
    primary_channel.set_volume(0.5)

def stop_primary_bgm(_fade_ms: float = 0.0):
    global primary_channel

    if not primary_channel.get_busy():
        return
    
    primary_channel.stop(_fade_ms)

def pause_primary_bgm(_fade_ms: float = 0.0):
    global primary_channel

    if not primary_channel.get_busy():
        return
    
    primary_channel.pause()

def unpause_primary_bgm(_fade_ms: float = 0.0):
    pass

def play_secondary_bgm(_bgm: pygame.mixer.Sound):
    global primary_channel
    global secondary_channel
    
    global current_bgm_type
    global previous_bgm_type
    
    if primary_channel.get_busy():
        primary_channel.pause()
    
    current_bgm_type, previous_bgm_type = EBGMState.SECONDARY, current_bgm_type
    
    secondary_channel.play(_bgm)
    secondary_channel.set_volume(0.5)

def play_jingle_bgm(_bgm: pygame.mixer.Sound):
    global primary_channel
    global secondary_channel
    global jingle_channel

    global current_bgm_type
    global previous_bgm_type
    
    if primary_channel.get_busy():
        primary_channel.pause()

    if secondary_channel.get_busy():
        secondary_channel.pause()

    current_bgm_type, previous_bgm_type = EBGMState.JINGLE, current_bgm_type
    jingle_channel.play(_bgm)
    jingle_channel.set_volume(0.5)
    jingle_channel.set_endevent()

def update_bgm_state():
    global current_bgm_type
    global previous_bgm_type

    if current_bgm_type is EBGMState.JINGLE and not jingle_channel.get_busy():
        current_bgm_type, previous_bgm_type = previous_bgm_type, current_bgm_type
        primary_channel.unpause()

    print(f"{current_bgm_type}, {previous_bgm_type}")

test_bgm_1 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss0.wav")
test_bgm_2 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss1.wav")
test_bgm_3 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_NewScore.wav")