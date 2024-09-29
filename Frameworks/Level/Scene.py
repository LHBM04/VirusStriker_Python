from abc import ABC, abstractmethod
from typing import final
import queue

from Core.System import *
from Core.Object import *
from Utilities.Singleton import *

class Scene:
    def __init__(self, _sceneName: str) -> None:
        self.sceneName: str                 = _sceneName        # 해당 Scene의 이름. (나중에 Key로 사용할 것임.)

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
class SceneManager(metaclass = Singleton):
    def __init__(self) -> None:
        # -------------------[private field]------------------- #

        self.m_scenes: dict[str:Scene]      = {}                    # 관리할 Scene들.
        self.m_currentScene: Scene          = None                  # 현재 활성화된 Scene.
        self.m_nextScene: Scene             = None                  # 이동 중인 Scene
        self.m_previousScenes: queue[Scene] = queue.Queue()         # 이전에 활성화되었던 Scene들. (돌아가기 위함.)
        
        self.m_loadingBackground: Sprite            = Sprite("Resources/Sprites/Backgrounds/Loading/Logo")    # 로딩 백그라운드
        self.m_loadingBackgroundInfo: SpriteInfo    = SpriteInfo(Vector2(0, 0), 
                                                                 Vector2(1280, 800),
                                                                 0.0,
                                                                 False,
                                                                 False,
                                                                 Color())  # 로딩 백그라운드 스프라이트 정보

        self.isResetDeltaTime: bool = False                       # 델타 타임 리셋 여부.

    # -------------------[Scene Attributes]------------------- # 

    def GetActiveScene(self) -> Scene:
        if self.m_currentScene is None:
            assert(0)
            return
        
        return self.m_currentScene
    
    def AddScene(self, _sceneName: str, _scene: Scene) -> None:
        if _sceneName in self.m_scenes.keys() and _scene in self.m_scenes.values():
            assert(0)
            return
        
        self.m_scenes[_sceneName] = _scene

    def LoadScene(self, _sceneName: str) -> None:
        if len(self.m_scenes) <= 0 or _sceneName not in self.m_scenes:
            assert(0)
            return
        if self.m_currentScene != None:
            self.m_currentScene.OnExit()
            self.m_previousScenes.put(self.m_currentScene) # 현재 Scene은 이전의 Scene에 넣어준다.

        self.m_nextScene = self.m_scenes[_sceneName]

    def UnloadScene(self) -> None:
        if self.m_currentScene is None:
            assert(0)
            return
        
        try:
            self.m_currentScene.OnExit()
            self.m_nextScene = self.m_previousScenes.get()
            self.m_previousScenes.put(self.m_currentScene)
        except queue.Empty:
            global g_isRunning
            g_isRunning = False

    # -------------------[Game Loop]------------------- # 

    def Update(self, _deltaTime: float):
        self.isResetDeltaTime = False
        if self.m_nextScene != None:
            self.m_loadingBackgroundInfo.color.a = self.m_loadingBackgroundInfo.color.a + _deltaTime * 2.0
            if self.m_loadingBackgroundInfo.color.a >= Color.MAX_COLOR_VALUE:
                self.m_loadingBackgroundInfo.color.a = Color.MAX_COLOR_VALUE

                self.m_currentScene , self.m_nextScene = self.m_nextScene, None
                self.m_currentScene.OnEnter()
                self.isResetDeltaTime = True

        else:
            self.m_loadingBackgroundInfo.a = self.m_loadingBackgroundInfo.color.a - _deltaTime * 2.0
            if self.m_loadingBackgroundInfo.a <= Color.MIN_COLOR_VALUE:
                self.m_loadingBackgroundInfo.a = Color.MIN_COLOR_VALUE

        self.m_loadingBackground.Update(_deltaTime)
        
        if self.m_currentScene:
            self.m_currentScene.Update(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime: float):
       if self.m_currentScene:
            self.m_currentScene.FixedUpdate(_fixedDeltaTime)

    def RenderObject(self):
        if self.m_currentScene:
            self.m_currentScene.RenderObject()

    def RenderUI(self):
        if self.m_currentScene:
            self.m_currentScene.RenderUI()
