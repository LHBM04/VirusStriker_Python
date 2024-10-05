from enum import Enum

# Transition의 상태를 나타내는 열거형.
class ETransitionState(Enum):
    IDLE: int           = 0
    ENTER: int          = 1
    ENTERCOMPLETE: int  = 2
    EXIT: int           = 3
    EXITCOMPLETE: int   = 4