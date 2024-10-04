from collections import deque as stack
from typing import final, Dict

from Core.Utilities.Singleton import Singleton
from Level.SceneManagement.Scene import Scene

@final
class SceneManager(metaclass = Singleton):
    def __init__(self) -> None:
        # -------------------[private field]------------------- #
        self.__levels: Dict[str:Scene]      = {}  # 관리할 Scene들.
        self.__currentLevel: Scene          = None  # 현재 활성화된 Level.
        self.__nextLevel: Scene             = None  # 이동 중인 Level
        self.__previousLevels: stack[Scene] = stack()  # 이전에 활성화되었던 Scene들. (돌아가기 위함.)


        #self.m_loadingBackground: Sprite     = Sprite(ResourceManager().GetImage("Resources\\Sprites\\Background\\Loading\\Logo"))
        #self.m_loadingBackground.position    = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        #self.m_loadingBackground.scale       = Vector2(get_canvas_width(), get_canvas_height())
        #self.m_loadingBackground.color       = Color(255, 255, 255, 0)

        self.isResetDeltaTime: bool = False  # 델타 타임 리셋 여부.
    # -------------------[Level Attributes]------------------- #

    def GetActiveLevel(self) -> Scene:
        if self.__currentLevel is None:
            assert (0)

        return self.__currentLevel

    def AddLevel(self, _levelName: str, _scene: Scene) -> None:
        if _levelName in self.__levels.keys() and _scene in self.__levels.values():
            raise ValueError("[Oops!] 이미 존재하는 Scene입니다.")

        self.__levels[_levelName] = _scene

    def LoadLevel(self, _sceneName: str) -> None:
        if len(self.__previousLevels) > 0:
            self.__previousLevels[0].OnExit()

        #self.m_loadingBackground.isActive = True
        #self.m_loadingBackground.Render()

        self.__nextLevel = self.__levels[_sceneName]
        self.__previousLevels.append(self.__nextLevel)

    def UnloadLevel(self) -> None:
        if len(self.__previousLevels) <= 0:
            return

        self.__previousLevels.pop().OnExit()
        if len(self.__previousLevels) > 0:
            #self.m_loadingBackground.isActive = True
            #self.m_loadingBackground.Render()

            self.__nextLevel = self.__previousLevels[0]

    # -------------------[Game Loop]------------------- #

    def Update(self, _deltaTime: float):
        self.isResetDeltaTime = False
        if self.__nextLevel is not None:
            #self.m_loadingBackground.Update(_deltaTime)
            #self.m_loadingBackground.renderInfo.color.a += _deltaTime * 200.0
            #if self.m_loadingBackground.renderInfo.color.a >= Color.MaxValue():
                #self.m_loadingBackground.renderInfo.color.a = Color.MaxValue()

                self.__currentLevel, self.__nextLevel = self.__nextLevel, None
                self.__currentLevel.OnEnter()

                self.isResetDeltaTime = True
        else:
            #self.m_loadingBackground.renderInfo.color.a -= _deltaTime * 200.0
            #if self.m_loadingBackground.renderInfo.color.a <= Color.MinValue():
                #self.m_loadingBackground.renderInfo.color.a = Color.MinValue()
                #self.m_loadingBackground.isActive = False
            pass

        if self.__currentLevel is not None:
            self.__currentLevel.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        if self.__currentLevel is not None:
            self.__currentLevel.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self):
        if self.__currentLevel is not None:
            self.__currentLevel.RenderObject()

    def RenderUI(self):
        if self.__currentLevel is not None:
            self.__currentLevel.RenderUI()

        #self.m_loadingBackground.Render()
