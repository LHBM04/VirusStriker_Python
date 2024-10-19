from typing import final, Optional, Dict, Any

from pico2d import *

from Core.Utilities.Singleton import Singleton

@final
class AudioChannel:
    def __init__(self):
        self.__audioClip: Optional[Music]   = None
        self.__isPlaying: bool              = False

        self.__isLoop: bool = False
        self.__time: float  = 0.0

        self.__MAX_VOLUME: float    = 1.0
        self.__MIN_VOLUME: float    = 0.0
        self.__volume: float        = self.__MAX_VOLUME / 2.0

# region Properties
    @property
    def audio(self) -> Music:
        return self.__audioClip

    @audio.setter
    def audio(self, _value: Music) -> None:
        self.__audioClip = _value

    @property
    def isPlaying(self) -> bool:
        return self.__isPlaying

    @property
    def isLoop(self) -> bool:
        return self.__isLoop

    @isLoop.setter
    def isLoop(self, _value) -> None:
        self.__isLoop = _value

    @property
    def time(self) -> float:
        return self.__time

    @time.setter
    def time(self, _value: float) -> None:
        self.__time = _value

    @property
    def volume(self) -> float:
        return self.__volume

    @volume.setter
    def volume(self, _value: float) -> None:
        self.__volume = min(self.__MAX_VOLUME, max(self.__MIN_VOLUME, _value))

# endregion

@final
class LoopAudioChannel:
    def __init__(self, _audioChannel: AudioChannel):
        self.__audioChannel: AudioChannel   = _audioChannel
        self.__loopStart: float             = 0.0
        self.__loopEnd: float               = 999.9

# region Properties
    @property
    def loopStart(self) -> float:
        return self.__loopStart

    @property
    def loopEnd(self) -> float:
        return self.__loopEnd

# endregion
    def Reset(self) -> None:
        self.__loopStart            = 0.0
        self.__loopEnd              = 0.0

    def SetFrom(self, _music, _loopData) -> None:
        self.__loopStart            = _loopData.loopStart
        self.__loopEnd              = _loopData.loopEnd

@final
class AudioManager(metaclass = Singleton):
    def __init__(self):
        self.__currentBGM: Optional[Music]  = None
        self.__previousBGM: Optional[Music] = None

        self.__bgmVolume: float             = 0

        self.__bgmLoopTimer: float          = 0.0

        self.__currentSFX:Optional[Music] = None
        self.__sfxVolume: float = 0

    def Update(self, _deltaTime: float) -> None:
        if not self.__currentBGM:
            return


