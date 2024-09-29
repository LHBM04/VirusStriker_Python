import pygame
from enum import Enum

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

def PlayPrimaryBGM(_bgm: pygame.mixer.Sound, _is_loop: bool = True, _fade_ms: int = 0):
    global primaryChannel
   
    global currentBGMType
    global previousBGMType
 
    currentBGMType, previousBGMType = EBGMState.PRIMARY, currentBGMType 

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
    pass

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

def UpdateBGMState():
    global currentBGMType
    global previousBGMType

    if currentBGMType is EBGMState.JINGLE and not jingleChannel.get_busy():
        currentBGMType, previousBGMType = previousBGMType, currentBGMType
        primaryChannel.unpause()

testBGM1 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Invincible.wav")
testBGM2 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_Boss1.wav")
testBGM3 = pygame.mixer.Sound("Resources/Audio/BGM/BGM_NewScore.wav")