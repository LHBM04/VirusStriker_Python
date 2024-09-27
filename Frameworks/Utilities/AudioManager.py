import pygame
from pygame import *
from Utilities.Singleton import Singleton
from enum import Enum, auto

# 오디오(BGM/SFX)를 재생하는 매니저 클래스.
class AudioManager(Singleton):
    # BGM
    DEFAULT_BGM_VOLUME  = 0.5   # 기본 BGM 볼륨.
    m_bgmVolume         = None  # BGM 볼륨.

    m_primarySource     = None      # 일반 BGM 재생용 소스. (메인)
    m_secondarySource   = None      # 특수 상황용 BGM 재생용 소스. (서브)
    m_jingleSource      = None      # 징글 BGM 재생용 소스.

    class EPlayMode(Enum):
        LOOP    = -1,
        NOTLOOP = 0,

    # SFX
    DEFAULT_SFX_VOLUME  = 0.5   # 기본 SFX 볼륨.
    m_sfxVolume         = None  # SFX 볼륨.

    m_sfxSources = { None, }      # SFX 재생용 소스들.
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.m_bgmVolume = self.DEFAULT_BGM_VOLUME
        self.m_sfxVolume = self.DEFAULT_SFX_VOLUME

    # 게임 내 사용할 오디오 데이터를 생성합니다.
    def CreateAudio(self, _path):
        return pygame.mixer.Sound(_path)

    # 모든 BGM 소스들을 리셋합니다.
    def ResetBGM(self):
        self.m_primarySource.stop()
        self.m_primarySource = None
        
        self.m_secondarySource.stop()
        self.m_secondarySource = None
        
        self.m_jingleSource.stop()
        self.m_jingleSource = None

    # 게임 내 메인 BGM을 재생합니다.
    def PlayPrimaryBGM(self, _bgm, _isLoop = -1):
        self.m_primarySource = _bgm
        self.m_primarySource.set_volume(self.m_bgmVolume)
        self.m_primarySource.play(_isLoop)

    def StopPrimaryBGM(self):
        self.m_primarySource.stop()
    
