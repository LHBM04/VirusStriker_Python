# TODO: AudioSystem 개발 과정
# 1. 메인 BGM 재생/정지 함수 만들기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 2. 서브 BGM 재생/정지 함수 작성하기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 3. 징글 BGM 재생/정지 함수 작성하기
#   - 일시 정지/정지된 시점 재생 구현
#   - 페이드 효과 재생/정지 구현
# 4. SFX 재생 로직 작성하기 
#   - 재생 위치 다르게 하기
#   - 오브젝트 풀링 이용해서 SFX 재생 소스 할당하기
import pygame

pygame.mixer.init()

current_bgm_type: int = None

primary_channel: pygame.mixer.Channel   = pygame.mixer.Channel(0)
secondary_channel: pygame.mixer.Channel = pygame.mixer.Channel(1)
jingle_channel: pygame.mixer.Channel    = pygame.mixer.Channel(2)

def play_primary_bgm(_bgm: pygame.mixer.Sound):
    primary_channel.play(_bgm)
    primary_channel.set_volume(0.5)

def play_secondary_bgm(_bgm: pygame.mixer.Sound):
    if primary_channel.get_busy():
        primary_channel.pause()
    
    secondary_channel.play(_bgm)
    secondary_channel.set_volume(0.5)

def play_jingle_bgm(_bgm: pygame.mixer.Sound):
    global current_bgm_type
    
    if primary_channel.get_busy():
        primary_channel.pause()

    if secondary_channel.get_busy():
        secondary_channel.pause()

    current_bgm_type = 3
    jingle_channel.play(_bgm)
    jingle_channel.set_volume(0.5)
    jingle_channel.set_endevent()

def update_bgm_state():
    global current_bgm_type

    if current_bgm_type is 3 and not jingle_channel.get_busy():
        current_bgm_type = 1
        primary_channel.play(test_bgm_1, 0, 0, 10)

test_bgm_1 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss0.wav")
test_bgm_2 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss1.wav")
test_bgm_3 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_NewScore.wav")