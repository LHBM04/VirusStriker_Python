from abc import ABC, abstractmethod
from typing import final

from Core.Vector2 import *
from Core.Sprite import *

# 게임 내 사용되는 모든 오브젝트의 베이스 클래스.
class Object(ABC):
    def __init__(self) -> None:
        self.position = Vector2(0.0, 0.0)
        self.collisionLayer = 0
        self.renderLayer = 0
        self.isDestroied = False
        self.colisionTag = "None"

    # -----------[추상 메서드]-------------- #

    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        pass
    
    @abstractmethod
    def LateUpdate(self, _deltaTime: float) -> None:
        pass
    
    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass
    
    @abstractmethod
    def Render(self) -> None:
        pass

    @abstractmethod
    def RenderDebug(self) -> None:
        pass

# 오브젝트의 상태를 감시하고, 관리하는 매니저.
@ final
class ObjectManager:
    def __init__(self) -> None:
        self.m_addObjects: list[Object] = {}    # 추가할 오브젝트 리스트.
        self.m_objects: list[Object] = {}       # 관리 중인 오브젝트 리스트.

    # 관리할 오브젝트를 추가합니다.
    def AddObject(self, _newObject: Object) -> None:
        self.m_addObjects.append(_newObject)

    # 관리하는 오브젝트들의 Update()를 실행합니다.
    def Update(self, _deltaTime: float) -> None:
        if len(self.m_addObjects) > 0:
            self.m_objects.append(self.m_addObjects)
            self.m_addObjects.clear()

        if len(self.m_objects) > 0:
            self.m_objects.sort(lambda object : object.renderLayer)
            for object in self.m_objects:
                object.Update(_deltaTime)

            for object in self.m_objects:
                object.LateUpdate(_deltaTime)
        
    # 관리하는 오브젝트들의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        if len(self.m_objects) > 0:
            toRemove: list[Object] = []
        
            for object in self.m_objects:
                object.FixedUpdate(_fixedDeltaTime) 
            if object.isDestroied:
                toRemove.append(object) 

            for object in toRemove:
                self.m_objects.remove(object)

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if len(self.m_objects) > 0:
            for object in self.m_objects:
                object.Render()
                object.RenderDebug()