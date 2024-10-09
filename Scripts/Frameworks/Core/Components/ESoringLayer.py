from enum import Enum

# 그려야 할 그래픽들의 우선 순위를 나타내는 열거형. (가장 높은 것이 우선 순위)
class ESortingLayer(Enum):
    NONE = 0
    BACKGROUND = 1
    FOREGROUND = 2
    OBJECT = 3
    UI = 4