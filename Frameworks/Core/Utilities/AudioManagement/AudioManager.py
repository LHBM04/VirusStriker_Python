from typing import final

from pygame import *
from pygame.mixer import *

from Frameworks.Core.Utilities import Singleton

@final
class AudioManager(metaclass = Singleton):
    def __init__(self):
        pass