from abc import ABC, abstractmethod
from collections import deque as stack
from typing import final, Dict

from Core.Utilities.Singleton import Singleton

class Scene(ABC):
    def __init__(self) -> None:
        from Core.Components.GameObject import GameObjectManager

        self.objectManager: GameObjectManager   = GameObjectManager()   # 해당 Level 내 오브젝트를 관리하는 매니저 인스턴스
        self.uiManager: GameObjectManager       = GameObjectManager()   # 해당 Level 내 UI를 관리하는 매니저 인스턴스

    # -------------------[virtual methods]------------------- #

    def Update(self, _deltaTime: float) -> None:
        self.objectManager.Update(_deltaTime)
        self.uiManager.Update(_deltaTime)

        self.OnUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.objectManager.FixedUpdate(_fixedDeltaTime)
        self.uiManager.FixedUpdate(_fixedDeltaTime)

        self.OnFixedUpdate(_fixedDeltaTime)

    def RenderObject(self) -> None:
        self.objectManager.Render()
        self.OnRender()

    def RenderUI(self) -> None:
        self.uiManager.Render()
        self.OnUIRender()

    # -------------------[abstract methods]------------------- #

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
    def OnExit(self) -> None:
        pass

    @abstractmethod
    def OnRender(self) -> None:
        pass

    @abstractmethod
    def OnUIRender(self) -> None:
        pass

@final
class SceneManager(metaclass = Singleton):
    def __init__(self) -> None:
        # -------------------[private field]------------------- #
        self.m_levels: Dict[str:'Scene']      = {}  # 관리할 Scene들.
        self.m_currentLevel: 'Scene'          = None  # 현재 활성화된 Level.
        self.m_nextLevel: 'Scene'             = None  # 이동 중인 Level
        self.m_previousLevels: stack['Scene'] = stack()  # 이전에 활성화되었던 Scene들. (돌아가기 위함.)

        #self.m_loadingBackground: Sprite     = Sprite(ResourceManager().GetImage("Resources\\Sprites\\Background\\Loading\\Logo"))
        #self.m_loadingBackground.position    = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        #self.m_loadingBackground.scale       = Vector2(get_canvas_width(), get_canvas_height())
        #self.m_loadingBackground.color       = Color(255, 255, 255, 0)

        self.isResetDeltaTime: bool = False  # 델타 타임 리셋 여부.
    # -------------------[Level Attributes]------------------- #

    def GetActiveLevel(self) -> Scene:
        if self.m_currentLevel is None:
            assert (0)

        return self.m_currentLevel

    def AddLevel(self, _levelName: str, _scene: Scene) -> None:
        if _levelName in self.m_levels.keys() and _scene in self.m_levels.values():
            raise ValueError("[Oops!] 이미 존재하는 Scene입니다.")

        self.m_levels[_levelName] = _scene

    def LoadLevel(self, _sceneName: str) -> None:
        if len(self.m_previousLevels) > 0:
            self.m_previousLevels[0].OnExit()

        #self.m_loadingBackground.isActive = True
        #self.m_loadingBackground.Render()

        self.m_nextLevel = self.m_levels[_sceneName]
        self.m_previousLevels.append(self.m_nextLevel)

    def UnloadLevel(self) -> None:
        if len(self.m_previousLevels) <= 0:
            return

        self.m_previousLevels.pop().OnExit()
        if len(self.m_previousLevels) > 0:
            #self.m_loadingBackground.isActive = True
            #self.m_loadingBackground.Render()

            self.m_nextLevel = self.m_previousLevels[0]

    # -------------------[Game Loop]------------------- #

    def Update(self, _deltaTime: float):
        self.isResetDeltaTime = False
        if self.m_nextLevel is not None:
            #self.m_loadingBackground.Update(_deltaTime)
            #self.m_loadingBackground.renderInfo.color.a += _deltaTime * 200.0
            #if self.m_loadingBackground.renderInfo.color.a >= Color.MaxValue():
                #self.m_loadingBackground.renderInfo.color.a = Color.MaxValue()

                self.m_currentLevel, self.m_nextLevel = self.m_nextLevel, None
                self.m_currentLevel.OnEnter()

                self.isResetDeltaTime = True
        else:
            #self.m_loadingBackground.renderInfo.color.a -= _deltaTime * 200.0
            #if self.m_loadingBackground.renderInfo.color.a <= Color.MinValue():
                #self.m_loadingBackground.renderInfo.color.a = Color.MinValue()
                #self.m_loadingBackground.isActive = False
            pass

        if self.m_currentLevel is not None:
            self.m_currentLevel.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
        if self.m_currentLevel is not None:
            self.m_currentLevel.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self):
        if self.m_currentLevel is not None:
            self.m_currentLevel.RenderObject()

    def RenderUI(self):
        if self.m_currentLevel is not None:
            self.m_currentLevel.RenderUI()

        #self.m_loadingBackground.Render()
