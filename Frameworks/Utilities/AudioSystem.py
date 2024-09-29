from enum import Enum

import pygame

pygame.mixer.init() # pygame.mixer 초기화.

# 재생 중인 BGM의 타입을 나타내는 열거형.
class EBGMState(Enum):
    NONE        = 0
    PRIMARY     = 1
    SECONDARY   = 2
    JINGLE      = 3

currentBGMType: EBGMState     = EBGMState.NONE    # 현재 재생 중인 BGM의 타입.
previousBGMType: EBGMState    = EBGMState.NONE    # 이전에 재생 중이었던 BGM의 타입.

primaryChannel: pygame.mixer.Channel   = pygame.mixer.Channel(0)   # 메인 BGM의 재생 채널
secondaryChannel: pygame.mixer.Channel = pygame.mixer.Channel(1)   # 서브 BGM의 재생 채널
jingleChannel: pygame.mixer.Channel    = pygame.mixer.Channel(2)   # 징글 BGM의 재생 채널

def UpdateBGMState():
    global currentBGMType
    global previousBGMType

    if currentBGMType is EBGMState.JINGLE and not jingleChannel.get_busy():
        currentBGMType, previousBGMType = previousBGMType, currentBGMType
        ReplayPrimaryBGM()

    # print(f"current: {currentBGMType}, previous: {previousBGMType}")

def PlayPrimaryBGM(_bgm: pygame.mixer.Sound, _is_loop: bool = True, _fade_ms: int = 0):
    global primaryChannel
   
    global currentBGMType
    global previousBGMType
 
    currentBGMType, previousBGMType = EBGMState.PRIMARY, None 

    primaryChannel.play(_bgm, -1 if _is_loop is True else 0, 0, _fade_ms)
    primaryChannel.set_volume(0.5)

def StopPrimaryBGM(_fade_ms: float = 0.0):
    global primaryChannel

    if not primaryChannel.get_busy():
        return
    
    primaryChannel.stop(_fade_ms)

def PausePrimaryBGM(_fade_ms: float = 0.0):
    global primaryChannel

    if not primaryChannel.get_busy():
        return
    
    primaryChannel.pause()

def ReplayPrimaryBGM(_fade_ms: float = 0.0):
    global currentBGMType
    global previousBGMType

    currentBGMType, previousBGMType = EBGMState.PRIMARY, None
    primaryChannel.unpause()

def PlaySecondaryBGM(_bgm: pygame.mixer.Sound):
    global primaryChannel
    global secondaryChannel
    
    global currentBGMType
    global previousBGMType
    
    if primaryChannel.get_busy():
        primaryChannel.pause()
    
    currentBGMType, previousBGMType = EBGMState.SECONDARY, currentBGMType
    
    secondaryChannel.play(_bgm)
    secondaryChannel.set_volume(0.5)

def PlayJingle(_bgm: pygame.mixer.Sound):
    global primaryChannel
    global secondaryChannel
    global jingleChannel

    global currentBGMType
    global previousBGMType
    
    if primaryChannel.get_busy():
        primaryChannel.pause()

    if secondaryChannel.get_busy():
        secondaryChannel.pause()

    currentBGMType, previousBGMType = EBGMState.JINGLE, currentBGMType
    jingleChannel.play(_bgm)
    jingleChannel.set_volume(0.5)
    jingleChannel.set_endevent()

DEFAULT_SFX_VOLUME: float   = 0.5
g_sfxVolume: float          = DEFAULT_SFX_VOLUME

g_maxConcurrentSFXCount = 16
g_startIdex = 4

g_sfxChannels: set[pygame.mixer.Channel] = set()

def CreateSFXSource() -> pygame.mixer.Channel:
    g_sfxChannels.add(pygame.mixer.Channel(g_maxConcurrentSFXCount = g_maxConcurrentSFXCount + 1))
    return g_sfxChannels(g_maxConcurrentSFXCount)

def InitializeSFXSource() -> None:
    for index in range(g_startIdex, (g_startIdex + g_maxConcurrentSFXCount) + 1):
        g_sfxChannels.append(pygame.mixer.Channel(index))

def PlaySFX(_sfx: pygame.mixer.Sound) -> None: 
    available_channel = next((ch for ch in g_sfxChannels if not ch.get_busy()), None)
    
    if available_channel:
        available_channel.play(_sfx, 0, 0, 0)
    else:
        available_channel = CreateSFXSource(_sfx, 0, 0, 0)

testBGM1 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Invincible.wav")
testBGM2 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss1.wav")
testBGM3 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_NewScore.wav")

testSFX1 = pygame.mixer.Sound("Resources/Audio/SFX/SFX_EnemyDead1.wav")
testSFX2 = pygame.mixer.Sound("Resources/Audio/SFX/SFX_EnemyDead2.wav")
testSFX3 = pygame.mixer.Sound("Resources/Audio/SFX/SFX_EnemyDead3.wav")