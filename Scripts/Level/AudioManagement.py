from typing import final

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
