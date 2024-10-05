from abc import ABCMeta, abstractmethod

class Animation(metaclass = ABCMeta):
    def __init__(self):
        self.__isLoop: bool = False  # 해당 스프라이트의 루프 여부.
        self.__isEnd: bool = False  # 해당 스프라이트의 루프 종료 여부.
        self.__animationTime: float = 0.1  # 해당 스프라이트의 애니메이션 시간.
        self.__animationDeltaTime: float = 0.0  # 해당 스프라이트의 애니메이션 루프에 사용될 타이머.



    @property
    def isLoop(self) -> bool:
        return self.__isLoop

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @abstractmethod
    def Update(self, _deltaTime: float):
        pass

    @abstractmethod
    def Render(self):
        pass