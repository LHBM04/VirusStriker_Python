from enum import Enum

import pygame
from Utilities.Singleton import *

# 재생 중인 BGM의 타입을 나타내는 열거형.
class EBGMState(Enum):
    NONE        = 0
    PRIMARY     = 1
    SECONDARY   = 2
    JINGLE      = 3

class AudioManager(metaclass = Singleton):
    def __init__(self) -> None:
        pygame.mixer.init() # pygame.mixer 초기화.

        self.DEFAULT_BGM_VOLUME: float = 0.5
        self.bgmVolume: float = self.DEFAULT_BGM_VOLUME

        self.currentBGMType: EBGMState     = EBGMState.NONE    # 현재 재생 중인 BGM의 타입.
        self.previousBGMType: EBGMState    = EBGMState.NONE    # 이전에 재생 중이었던 BGM의 타입.

        self.primaryChannel: pygame.mixer.Channel   = pygame.mixer.Channel(0)   # 메인 BGM의 재생 채널
        self.secondaryChannel: pygame.mixer.Channel = pygame.mixer.Channel(1)   # 서브 BGM의 재생 채널
        self.jingleChannel: pygame.mixer.Channel    = pygame.mixer.Channel(2)   # 징글 BGM의 재생 채널

        self.DEFAULT_SFX_VOLUME: float = 0.5
        self.sfxVolume: float = self.DEFAULT_SFX_VOLUME

        self.maxConcurrentSFXCount = 5
        self.startIdex = 4

        self.sfxChannels: list[pygame.mixer.Channel] = []  # 리스트로 초기화

    def Update(self):
        if self.currentBGMType is EBGMState.JINGLE and not self.jingleChannel.get_busy():
            currentBGMType, previousBGMType = previousBGMType, currentBGMType
            self.ReplayPrimaryBGM()

        # [디버그용 코드]
        # print(f"current: {currentBGMType}, previous: {previousBGMType}")

    def PlayPrimaryBGM(self, _bgm: pygame.mixer.Sound, _is_loop: bool = True, _fade_ms: int = 0):
        self.currentBGMType, self.previousBGMType = EBGMState.PRIMARY, None 

        self.primaryChannel.play(_bgm, -1 if _is_loop is True else 0, 0, _fade_ms)
        self.primaryChannel.set_volume(0.5)

    def StopPrimaryBGM(self, _fade_ms: float = 0.0):
        if not self.primaryChannel.get_busy():
            return
    
        self.primaryChannel.stop(_fade_ms)

    def PausePrimaryBGM(self):
        if not self.primaryChannel.get_busy():
            return
    
        self.primaryChannel.pause()

    def ReplayPrimaryBGM(self):
        self.currentBGMType, self.previousBGMType = EBGMState.PRIMARY, None
        self.primaryChannel.unpause()

    def PlaySecondaryBGM(self, _bgm: pygame.mixer.Sound):
        if self.primaryChannel.get_busy():
            self.primaryChannel.pause()
    
        self.currentBGMType, self.previousBGMType = EBGMState.SECONDARY, self.currentBGMType
    
        self.secondaryChannel.play(_bgm)
        self.secondaryChannel.set_volume(0.5)

    def PlayJingle(self, _bgm: pygame.mixer.Sound):
        if self.primaryChannel.get_busy():
            self.primaryChannel.pause()

        if self.secondaryChannel.get_busy():
            self.secondaryChannel.pause()

        self.currentBGMType, self.previousBGMType = EBGMState.JINGLE, self.currentBGMType
        self.jingleChannel.play(_bgm)
        self.jingleChannel.set_volume(0.5)
        self.jingleChannel.set_endevent()


    def CreateSFXSource(self) -> pygame.mixer.Channel:
        self.g_maxConcurrentSFXCount += 1
        new_channel = pygame.mixer.Channel(self.maxConcurrentSFXCount)
        self.sfxChannels.append(new_channel)  # 리스트에 추가
        return new_channel  

    def InitializeSFXSource(self) -> None:
        for index in range(self.startIdex, self.startIdex + self.maxConcurrentSFXCount):
            self.sfxChannels.append(pygame.mixer.Channel(index))

    def PlaySFX(self, _sfx: pygame.mixer.Sound) -> None:
        sfxChannel = next((ch for ch in self.sfxChannels if not ch.get_busy()), self.CreateSFXSource())
        sfxChannel.set_volume(self.sfxVolume)
        sfxChannel.play(_sfx, 0, 0, 0)