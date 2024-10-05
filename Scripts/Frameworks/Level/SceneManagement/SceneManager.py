from collections import deque as stack
from typing import final, Dict

from Core.Utilities.Singleton import Singleton
from Level.SceneManagement.Scene import Scene
from Level.SceneManagement.SceneTransition import SceneTransition


@final
class SceneManager(metaclass = Singleton):
    def __init__(self) -> None:
        # -------------------[private field]------------------- #
        self.__scenes: Dict[str:Scene] = {}  # 관리할 Scene들.
        self.__currentScene: Scene = None  # 현재 활성화된 Level.
        self.__nextScene: Scene = None  # 이동 중인 Level
        self.__previousScenes: stack[Scene] = stack()  # 이전에 활성화되었던 Scene들. (돌아가기 위함.)

        self.__sceneTransition: SceneTransition = SceneTransition()
        self.isResetDeltaTime: bool = False  # Scene 로드 중일 때 시간을 멈추기.
    # -------------------[Level Attributes]------------------- #

    def GetActiveLevel(self) -> Scene:
        if self.__currentScene is None:
            assert (0)

        return self.__currentScene

    def AddLevel(self, _levelName: str, _scene: Scene) -> None:
        if _levelName in self.__scenes.keys() and _scene in self.__scenes.values():
            raise ValueError("[Oops!] 이미 존재하는 Scene입니다.")

        self.__scenes[_levelName] = _scene

    def LoadLevel(self, _sceneName: str) -> None:
        if len(self.__previousScenes) > 0:
            self.__previousScenes[0].OnExit()

        self.__nextScene = self.__scenes[_sceneName]
        self.__previousScenes.append(self.__nextScene)

        self.__sceneTransition.GoTo(self.__nextScene.name, self.ChangeScene)

    def ChangeScene(self):
        self.__currentScene, self.__nextScene = self.__nextScene, None
        self.__currentScene.OnEnter()

    def UnloadLevel(self) -> None:
        if len(self.__previousScenes) <= 0:
            return

        self.__previousScenes.pop().OnExit()
        if len(self.__previousScenes) > 0:
            self.__sceneTransition.isActive = True
            self.__sceneTransition.Render()

            self.__nextScene = self.__previousScenes[0]

    # -------------------[Game Loop]------------------- #

    def Update(self, _deltaTime: float):
        SceneManager().isResetDeltaTime = False

        if self.__nextScene is not None:
            self.__sceneTransition.Update(_deltaTime)

        if self.__currentScene is not None:
            self.__currentScene.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        if self.__currentScene is not None:
            self.__currentScene.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self):
        if self.__currentScene is not None:
            self.__currentScene.RenderObject()

    def RenderUI(self):
        if self.__currentScene is not None:
            self.__currentScene.RenderUI()

        self.__sceneTransition.Render()
