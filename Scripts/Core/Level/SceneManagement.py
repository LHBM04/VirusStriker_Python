from abc import ABCMeta, abstractmethod
from collections import deque
from typing import final, Dict, Deque, Optional, Iterable

from Core.Utilities.Singleton import Singleton

class Scene(metaclass = ABCMeta):
    """
    게임 내 모든 Scene의 베이스 클래스.
    """
    def __init__(self) -> None:
        # TODO: Game Object, UI Object 컨테이너 생성하기
        pass

    @final
    def Enter(self):
        """
        해당 Scene에 진입했을 때 한번만 실행됩니다.
        """
        pass

    @final
    def Update(self, _deltaTime: float) -> None:
        """
        매 프레임마다 Scene의 정보를 업데이트 합니다.
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 간격(초 단위).
        """
        # TODO: Game Object, UI Object 컨테이너 업데이트하기
        pass

    @final
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        """
        일정한 주기마다 Scene의 정보를 업데이트 합니다.
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 간격(초 단위).
        """
        # TODO: Game Object, UI Object 컨테이너 업데이트하기
        pass

    @final
    def Render(self) -> None:
        """
        Scene 내 Game Object의 그래픽을 렌더링합니다.
        """
        # TODO: Game Object 컨테이너 Render() Invoke하기.
        pass

    @final
    def RenderUI(self) -> None:
        """
        Scene 내 UI Object의 그래픽을 렌더링합니다.
        """
        # TODO: UI Object 컨테이너 Render() Invoke하기.
        pass

    @final
    def Exit(self) -> None:
        """
        해당 Scene을 빠져나왔을 때 한번만 실행됩니다.
        :return:
        """
        pass

@final
class SceneManager(metaclass = Singleton):
    """
    게임 내 모든 Scene을 관리하고 제어합니다.
    """
    def __init__(self):
        self.__scenes: Dict[str,  Scene]        = dict()    # 관리하고 있는 Scene들.
        self.__currentScene: Optional[Scene]    = None      # 현재 활성화 상태인 Scene.
        self.__nextScene: Optional[Scene]       = None      # 이동할 다음 Scene.
        self.__previousScenes: Deque[Scene]     = deque()   # 이전 Scene들.
        self.__isResetDeltaTime: bool           = False     # Scene 이동 중 시간을 멈추기 위한 Flag.

    # region Properties
    @property
    def scenes(self) -> Iterable[Scene]:
        """
        관리하고 있는 모든 Scene을 반환합니다.
        :return: 관리하고 있는 모든 Scene.
        """
        return self.__scenes.values()

    @property
    def currentScene(self) -> Scene:
        """
        현재 활성화 상태인 Scene을 반환합니다.
        :return: 현재 활성화 중인 Scene.
        """
        return self.__currentScene

    @property
    def nextScene(self) -> Scene:
        """
        다음에 이동할 Scene을 반환합니다.
        :return: 다음에 이동할 Scene.
        """
        return self.__nextScene

    @property
    def previousScenes(self) -> Deque[Scene]:
        """
        이전에 활성화되었던 Scene들을 반환합니다.
        :return: 이전에 활성화되었던 Scene들.
        """
        return self.__previousScenes

    @property
    def isResetDeltaTime(self) -> bool:
        """
        Scene 이동 중 시간이 정지되었는지에 대한 여부를 반환합니다.
        :return: Scene 이동 중 시간이 정지되었는지에 대한 여부.
        """
        return self.__isResetDeltaTime
    # endregion
    # region Life-Cycle
    def Update(self, _deltaTime: float):
        """
        매 프레임마다 Scene을 업데이트합니다.
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 간격(초 단위).
        """
        SceneManager().__isResetDeltaTime = False

        if self.__nextScene is not None:
            self.__currentScene, self.__nextScene = self.__nextScene, None
            self.__currentScene.Enter()
        else:
            pass

        if self.__currentScene is not None:
            self.__currentScene.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        """
        고정된 주기마다 Scene을 업데이트합니다.
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 변화량(초 단위).
        """
        if self.__currentScene is not None:
            self.__currentScene.FixedUpdate(_fixedDeltaTime)

    def Render(self):
        """
        Scene 내 Object들을 렌더링합니다.
        :return:
        """
        if self.__currentScene is not None:
            self.__currentScene.Render()

    def RenderUI(self) -> None:
        """
        Scene 내 UI들을 렌더링합니다.
        :return:
        """
        if self.__currentScene is not None:
            self.__currentScene.RenderUI()
    # endregion
    def AddLevel(self, _levelName: str, _scene: Scene) -> None:
        """
        새로운 Scene을 추가합니다.
        :param _levelName: 추가할 Scene의 이름.
        :param _scene: 추가할 Scene의 인스턴스.
        """
        if (_levelName in self.__scenes.keys() and
            _scene in self.__scenes.values()):
            raise ValueError("[Oops!] 이미 존재하는 Scene입니다.")

        self.__scenes[_levelName] = _scene

    def LoadLevel(self, _sceneName: str) -> None:
        """
        해당 Scene으로 이동합니다.
        :param _sceneName: 이동할 Scene의 이름.
        """
        if self.__previousScenes:
            self.__previousScenes[0].Exit()

        self.__nextScene = self.__scenes[_sceneName]
        self.__previousScenes.append(self.__nextScene)

    def UnloadLevel(self) -> None:
        """
        지금 활성화되어 있는 Scene을 탈출하고, 이전 Scene으로 돌아갑니다.
        """
        if self.__previousScenes:
            return

        self.__previousScenes.pop().OnExit()
        if self.__previousScenes:
            self.__nextScene = self.__previousScenes[0]