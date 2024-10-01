from abc import ABC, abstractmethod
from typing import final
from collections import deque

from Core.System import *
from Core.Actors.Object import *
from Utilities.Singleton import *
from Utilities.Vector2 import *

class Level(ABC):
    def __init__(self, _levelName: str) -> None:
        self.levelName: str                 = _levelName        # 해당 Scene의 이름. (나중에 Key로 사용할 것임.)

        self.objectManager: ObjectManager = ObjectManager()   # 해당 Scene 내 오브젝트를 관리하는 매니저 인스턴스
        self.uiManager: ObjectManager     = ObjectManager()   # 해당 Scene 내 UI를 관리하는 매니저 인스턴스

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
    def OnRender(self) -> None:
        pass

    @abstractmethod
    def OnUIRender(self) -> None:
        pass

    @abstractmethod
    def OnExit(self) -> None:
        pass

@final
class LevelManager(metaclass = Singleton):
    def __init__(self) -> None:
        # -------------------[private field]------------------- #

        self.m_levels: dict[str:Level]      = {}                    # 관리할 Scene들.
        self.m_currentLevel: Level          = None                  # 현재 활성화된 Scene.
        self.m_nextLevel: Level             = None                  # 이동 중인 Scene
        self.m_previousLevels: deque[Level] = deque()               # 이전에 활성화되었던 Scene들. (돌아가기 위함.)
        
        self.m_loadingBackground: Object                = Object()
        self.m_loadingBackground.position               = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.m_loadingBackground.scale                  = Vector2(get_canvas_width(), get_canvas_height())
        self.m_loadingBackground.collider               = None
        self.m_loadingBackground.sprite                 = Sprite(self.m_loadingBackground, "Resources\\Sprites\\Backgrounds\\Loading\\Logo")    # 로딩 백그라운드
        self.m_loadingBackground.sprite.info.position   = Vector2(get_canvas_width() / 2, get_canvas_height() / 2)
        self.m_loadingBackground.sprite.info.scale      = Vector2(get_canvas_width(), get_canvas_height())
        self.m_loadingBackground.sprite.info.color      = Color(255, 255, 255, 0)

        self.isResetDeltaTime: bool = False                       # 델타 타임 리셋 여부.

    # -------------------[Scene Attributes]------------------- # 

    def GetActiveLevel(self) -> Level:
        if self.m_currentLevel is None:
            assert(0)
            return
        
        return self.m_currentLevel
    
    def AddLevel(self, _levelName: str, _scene: Level) -> None:
        if _levelName in self.m_levels.keys() and _scene in self.m_levels.values():
            assert(0)
            return
        
        self.m_levels[_levelName] = _scene

    def LoadLevel(self, _levelName: str) -> None:
        if len(self.m_previousLevels) > 0:
            self.m_previousLevels[0].OnExit()
        
        self.m_loadingBackground.isActive = True
        self.m_loadingBackground.Render()

        self.m_nextLevel = self.m_levels[_levelName]
        self.m_previousLevels.append(self.m_nextLevel)

    def UnloadLevel(self) -> None:
        if len(self.m_previousLevels) <= 0:
            return;

        self.m_previousLevels.pop().OnExit();
        if len(self.m_previousLevels) > 0:
            self.m_loadingBackground.isActive = True
            self.m_loadingBackground.Render()

            self.m_nextLevel = self.m_previousLevels[0]

    # -------------------[Game Loop]------------------- # 

    def Update(self, _deltaTime: float):
        self.isResetDeltaTime = False
        if self.m_nextLevel != None:
            self.m_loadingBackground.sprite.info.color.a += _deltaTime * 100.0
            if (self.m_loadingBackground.sprite.info.color.a >= Color.maxValue()):
                self.m_loadingBackground.sprite.info.color.a = Color.maxValue()

                self.m_currentLevel , self.m_nextLevel = self.m_nextLevel, None
                self.m_currentLevel.OnEnter()

                self.isResetDeltaTime = True
        else:
            self.m_loadingBackground.sprite.info.color.a -= _deltaTime * 100.0
            if self.m_loadingBackground.sprite.info.color.a <= Color.minValue():
                self.m_loadingBackground.sprite.info.color.a = Color.minValue()
                self.m_loadingBackground.isActive = False

        self.m_loadingBackground.sprite.Update(_deltaTime)
        
        if self.m_currentLevel != None:
            self.m_currentLevel.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
       if self.m_currentLevel != None:
            self.m_currentLevel.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self):
        if self.m_currentLevel != None:
            self.m_currentLevel.RenderObject()

    def RenderUI(self):
        if self.m_currentLevel != None:
            self.m_currentLevel.RenderUI()

        self.m_loadingBackground.Render()
