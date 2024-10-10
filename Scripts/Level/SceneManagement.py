from abc import ABCMeta, abstractmethod
from collections import deque as stack
from typing import final, Dict

from Core.Objects.GameObject import GameObjectManager


class Scene(metaclass = ABCMeta):
    def __init__(self):
        self.name = "New Scene"

        self.objMng = GameObjectManager()

    #region [virtual methods]
    def Update(self, _deltaTime: float) -> None:
        self.objMng.Update(_deltaTime)

        self.OnUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.objMng.FixedUpdate(_fixedDeltaTime)

        self.OnFixedUpdate(_fixedDeltaTime)
    #endregion
    #region [abstract methods]
    @abstractmethod
    def OnEnter(self) -> None:
        pass

    @abstractmethod
    def OnUpdate(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def OnFixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    @abstractmethod
    def Render(self):
        pass

    def RenderDebug(self):
        pass

    @abstractmethod
    def OnExit(self) -> None:
        pass
    #endregion

from Core.Utilities.Singleton import Singleton

@final
class SceneManager(metaclass = Singleton):
    def __init__(self) -> None:
        self.__scenes: Dict[str : Scene]    = {}  # 관리할 Scene들.
        self.__currentScene: Scene          = None  # 현재 활성화된 Level.
        self.__nextScene: Scene             = None  # 이동 중인 Level
        self.__previousScenes: stack[Scene] = stack()  # 이전에 활성화되었던 Scene들. (돌아가기 위함.)
        self.__isResetDeltaTime: bool       = False  # Scene 로드 중일 때 시간을 멈추기.

    #region [Properties]
    @property
    def scenes(self) -> Dict:
        return self.__scenes

    @property
    def currentScene(self) -> Scene:
        return self.__currentScene

    @property
    def nextScene(self) -> Scene:
        return self.__nextScene

    @property
    def priviouseScenes(self) -> stack[Scene]:
        return self.__previousScenes

    @property
    def isResetDeltaTime(self) -> bool:
        return self.__isResetDeltaTime
    #endregion
    #region [Methods]
    def AddLevel(self, _levelName: str, _scene: Scene) -> None:
        if _levelName in self.__scenes.keys() and _scene in self.__scenes.values():
            raise ValueError("[Oops!] 이미 존재하는 Scene입니다.")

        self.__scenes[_levelName] = _scene

    def LoadLevel(self, _sceneName: str) -> None:
        if len(self.__previousScenes) > 0:
            self.__previousScenes[0].OnExit()

        self.__nextScene = self.__scenes[_sceneName]
        self.__previousScenes.append(self.__nextScene)

    def UnloadLevel(self) -> None:
        if len(self.__previousScenes) <= 0:
            return

        self.__previousScenes.pop().OnExit()
        if len(self.__previousScenes) > 0:
            self.__nextScene = self.__previousScenes[0]
    #endregion
    #region [Life-Cycle]
    def Update(self, _deltaTime: float):
        SceneManager().__isResetDeltaTime = False

        if self.__nextScene is not None:
            self.__currentScene, self.__nextScene = self.__nextScene, None
            self.__currentScene.OnEnter()
        else:
            pass

        if self.__currentScene is not None:
            self.__currentScene.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        if self.__currentScene is not None:
            self.__currentScene.FixedUpdate(_fixedDeltaTime)

    def Render(self):
        if self.__currentScene is not None:
            self.__currentScene.Render()

    def RenderDebug(self):
        if self.__currentScene is not None:
            self.__currentScene.RenderDebug()
    #endregion
