import pygame

pygame.mixer.init()

DEFAULT_BGM_VOLUME  = 0.5
g_bgmVolume         = DEFAULT_BGM_VOLUME

g_primarySource     = None
g_secondarySource   = None
g_jingleSource      = None

def CreateAudio(_path) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(_path)

def PlayPrimaryBGM(_primaryBGM, _isLoop = True) -> None:
    global g_bgmVolume
    global g_primarySource
    
    if (g_primarySource is not None):
        g_primarySource.stop()
        g_primarySource =  None

    g_primarySource = _primaryBGM
    g_primarySource.set_volume(g_bgmVolume)
    g_primarySource.play(True if _isLoop else False)

def StopPrimaryBGM() -> None:
    global g_primarySource
    
    if (g_primarySource is not None):
        g_primarySource.stop()
        g_primarySource =  None

DEFAULT_SFX_VOLUME = 0.5
g_sfxVolume = DEFAULT_SFX_VOLUME