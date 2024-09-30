from abc import ABC, abstractmethod
from typing import final
from collections import deque

from Core.System import *
from Core.Actors.Object import *
from Utilities.Singleton import *

class Level(ABC):
    def __init__(self, _levelName: str) -> None:
        self.levelName: str                 = _levelName        # 해당 Scene의 이름. (나중에 Key로 사용할 것임.)

        self.m_objectManager: ObjectManager = ObjectManager()   # 해당 Scene 내 오브젝트를 관리하는 매니저 인스턴스
        self.m_uiManager: ObjectManager     = ObjectManager()   # 해당 Scene 내 UI를 관리하는 매니저 인스턴스

    # -------------------[virtual methods]------------------- #

    def Update(self, _deltaTime: float) -> None:
        self.m_objectManager.Update(_deltaTime)
        self.m_uiManager.Update(_deltaTime)

        self.OnUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self.m_objectManager.FixedUpdate(_fixedDeltaTime)
        self.m_uiManager.FixedUpdate(_fixedDeltaTime)

        self.OnFixedUpdate(_fixedDeltaTime)

    def RenderObject(self) -> None:
        self.m_objectManager.Render()
        self.OnRender()

    def RenderUI(self) -> None:
        self.m_uiManager.Render()
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
        
        self.m_loadingBackground: Sprite            = Sprite("Resources\\Sprites\\Backgrounds\\Loading\\Logo")    # 로딩 백그라운드
        self.m_loadingBackgroundInfo: SpriteInfo    = SpriteInfo(Vector2(0, 0), 
                                                                 Vector2(get_canvas_width(), get_canvas_height()),
                                                                 0.0,
                                                                 False,
                                                                 False,
                                                                 Color(255, 255, 255, 255))  # 로딩 백그라운드 스프라이트 정보

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
        
        self.m_nextLevel = self.m_levels[_levelName]
        self.m_previousLevels.append(self.m_nextLevel)

    def UnloadLevel(self) -> None:
        if len(self.m_previousLevels) <= 0:
            assert(0)
            return;

        self.m_previousLevels.pop().OnExit();
        if len(self.m_previousLevels) > 0:
            self.m_nextLevel = self.m_previousLevels[0]

    # -------------------[Game Loop]------------------- # 

    def Update(self, _deltaTime: float):
        self.isResetDeltaTime = False
        if self.m_nextLevel != None:
            self.m_loadingBackgroundInfo.color.a += _deltaTime * 2.0
            if self.m_loadingBackgroundInfo.color.a >= Color.maxValue():
                self.m_loadingBackgroundInfo.color.a = Color.maxValue()

                self.m_currentLevel , self.m_nextLevel = self.m_nextLevel, None
                self.m_currentLevel.OnEnter()
                self.isResetDeltaTime = True

        else:
            self.m_loadingBackgroundInfo.color.a -= _deltaTime * 2.0
            if self.m_loadingBackgroundInfo.color.a <= Color.minValue():
                self.m_loadingBackgroundInfo.color.a = Color.minValue()

        self.m_loadingBackground.Update(_deltaTime)
        
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
