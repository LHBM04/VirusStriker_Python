from typing import final

from sdl2 import *
from sdl2.sdlmixer import *

from Core.Utilities.Singleton import Singleton

@final
class AudioChannel:
    def __init__(self):
        ...

    def __del__(self):
        ...

@final
class AudioManager(metaclass = Singleton):
    def __init__(self):
        ...

    def __del__(self):
        ...
