from typing import final

from pico2d import *

from Core.Utilities.Singleton import Singleton
from Core.Utilities.InputManagement import InputManager

@final
class SystemManager(metaclass=Singleton):
    """
    시스템의 정보와 상태를 관리하고 제어합니다.
    """
    def __init__(self) -> None:
        self.__isGameRunning: bool = True              # 프로그램 구동 여부.
        self.__windowsTitle: str = "Virus Striker"     # 프로그램(윈도우) 이름.
        self.__windowsWidth: int = 1280                # 가로 해상도 (테스트).
        self.__windowsHeight: int = 720                # 세로 해상도 (테스트).

    @property
    def windowsTitle(self) -> str:
        """
        윈도우 제목을 반환합니다.
        :return: 윈도우 제목.
        """
        return self.__windowsTitle

    @property
    def windowsWidth(self) -> int:
        """
        윈도우 가로 해상도를 반환합니다.
        :return: 윈도우 가로 해상도.
        """
        return self.__windowsWidth

    @property
    def windowsHeight(self) -> int:
        """
        윈도우 세로 해상도를 반환합니다.
        :return: 윈도우 세로 해상도.
        """
        return self.__windowsHeight

    @property
    def isGameRunning(self) -> bool:
        """
        게임이 현재 실행 중인지 여부를 반환합니다.
        :return: 게임 실행 여부.
        """
        return self.__isGameRunning

    def Update(self, _deltaTime: float) -> None:
        """
        시스템 업데이트를 수행합니다.
        :param _deltaTime: 프레임 시간 간격.
        """
        InputManager().Update()

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        """
        고정 업데이트를 수행합니다.
        :param _fixedDeltaTime: 고정된 프레임 시간 간격.
        """
        pass

    def Render(self) -> None:
        """
        화면을 렌더링합니다.
        """
        clear_canvas()
        update_canvas()

    def CleanUp(self) -> None:
        """
        리소스를 정리하고 창을 닫습니다.
        """
        clear_canvas()
        close_canvas()

    def Quit(self) -> None:
        """
        게임을 종료합니다.
        """
        self.__isGameRunning = False
