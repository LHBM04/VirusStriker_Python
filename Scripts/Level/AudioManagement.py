from typing import final

from sdl2 import *
from sdl2.sdlmixer import *

from Core.Utilities.Singleton import Singleton

@final
class AudioManager(metaclass = Singleton):
    def __init__(self):
        self.__primaryChannel: int      = 0
        self.__secondaryChannel: int    = 1
        self.__jingleChannel: int       = 2

        self.__MAX_BGM_VOLUME: float    = 1.0
        self.__MIN_BGM_VOLUME: float    = 0.0
        self.__bgmVolume: float         = 0.5

        ## Initialize SDL audio
        #if SDL_Init(SDL_INIT_AUDIO) != 0:
        #    print(f"Failed to initialize SDL audio: {SDL_GetError()}")
        #    return
#
        ## Open the audio device
        #if Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, MIX_DEFAULT_CHANNELS, 1024) < 0:
        #    print(f"Failed to initialize audio: {Mix_GetError()}")
        #    return
#
        ## Set number of channels (should be after Mix_OpenAudio)
        #if Mix_AllocateChannels(MIX_CHANNELS) == 0:
        #    print(f"Failed to allocate channels: {Mix_GetError()}")

    def __del__(self):
        Mix_CloseAudio()
        Mix_Quit()

    @property
    def bgmVolume(self) -> float:
        return self.__bgmVolume

    @bgmVolume.setter
    def bgmVolume(self, _value: float) -> None:
        self.__bgmVolume = max(self.__MIN_BGM_VOLUME, min(self.__MAX_BGM_VOLUME, _value))

        Mix_Volume(self.__primaryChannel, int(self.__bgmVolume * 128))
        Mix_Volume(self.__secondaryChannel, int(self.__bgmVolume * 128))
        Mix_Volume(self.__jingleChannel, int(self.__bgmVolume * 128))

    def PlayPrimaryBGM(self, _bgm: Mix_Chunk) -> None:
       if Mix_PlayChannel(self.__primaryChannel, _bgm, True) == -1:
           print(f"Failed to play channel: {SDL_GetError()}")