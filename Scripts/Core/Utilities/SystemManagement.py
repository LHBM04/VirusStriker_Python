from typing import final

from pico2d import *

from Core.Level.SceneManagement import SceneManager
from Core.Utilities.InputManagement import InputManager
from Core.Utilities.Singleton import Singleton

@final
class SystemManager(metaclass = Singleton):
    """
    게임 내 중요 정보들을 관리하고, 게임 내 흐름을 제어합니다.
    """
    def __init__(self):
        self.__isGameRunning: bool = True               # 프로그램 구동 여부.

        self.__windowTitle: str     = "Virus Striker"   # 윈도우 창 타이틀.
        self.__windowWidth: int     = 1280              # 윈도우 창 폭.
        self.__windowHeight: int    = 720               # 윈도우 창 높이.
        self.__isFullScreen: bool   = False             # 전체 화면 여부.
        self.__isSync: bool         = True              # 수직 동기화 여부.

    # region Properties
    @property
    def window(self) -> SDL_Window:
        """
        해당 게임의 윈도우를 반환합니다.
        :return: 해당 게임의 윈도우.
        """
        return pico2d.window

    @property
    def renderer(self) -> SDL_Renderer:
        """
        해당 게임의 렌더러를 반환합니다.
        :return: 해당 게임의 렌더러.
        """
        return pico2d.renderer

    @property
    def windowTitle(self) -> str:
        """
        윈도우 창의 타이틀 이름을 반환합니다.
        :return: 윈도우 창의 상단 이름.
        """
        return self.__windowTitle

    @property
    def windowWidth(self) -> int:
        """
        윈도우 창의 폭을 반환합니다.
        :return: 윈도우 창의 폭.
        """
        return self.__windowWidth

    @property
    def windowHeight(self) -> int:
        """
        윈도우 창의 높이를 반환합니다.
        :return: 윈도우 창의 높이.
        """
        return self.__windowHeight

    @property
    def isFullScreen(self) -> bool:
        """
        윈도우 창의 풀 스크린 여부를 반환합니다.
        :return:
        """
        return self.__isFullScreen

    @property
    def isSync(self) -> bool:
        """
        윈도우 창의 수직 동기화 여부를 반환합니다.
        :return: 윈도우 창의 수직 동기화 여부.
        """
        return self.__isSync

    @property
    def isGameRunning(self) -> bool:
        """
        해당 게임의 구동 여부를 반환합니다.
        :return: 해당 게임의 구동 여부.
        """
        return self.__isGameRunning
    # endregion
    # region Life-Cycle
    def Update(self, _deltaTime: float) -> None:
        """
        매 프레임마다 실행되며 게임의 상태를 갱신합니다.
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 변화량(초 단위).
        """
        InputManager().Update()
        SceneManager().Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        """
        고정된 주기마다 실행되며 물리 연산 및 시간에 의존하는 처리를 수행합니다.
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 변화량(초 단위).
        """
        SceneManager().FixedUpdate(_fixedDeltaTime)
        pass

    def Render(self) -> None:
        """
        게임 내 그래픽을 렌더링하며 캔버스를 업데이트합니다.
        """
        clear_canvas()
        SceneManager().Render()
        SceneManager().RenderUI()
        update_canvas()

    def CleanUp(self) -> None:
        """
        게임 종료 시 리소스를 정리하고 캔버스를 닫습니다.
        """
        clear_canvas()
        close_canvas()
    # endregion
    def Quit(self):
        self.__isGameRunning = False
        print(self.__isGameRunning)

