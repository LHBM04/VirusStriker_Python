from abc import ABC, abstractmethod
from typing import final

from Core.Vector2 import *
from Core.Sprite import *

# 게임 내 사용되는 모든 오브젝트의 베이스 클래스.
class Object(ABC):
    def __init__(self) -> None:
        self.sprite: Sprite         = None
        self.spriteInfo: SpriteInfo = None
        
        self.position: Vector2   = Vector2()
        self.collisionLayer: int = 0
        self.renderLayer: int    = 0
        self.isDestroied: bool   = False
        self.colisionTag: str    = "None"

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
        self.m_addObjects: list[Object] = []  # 추가할 오브젝트 리스트.
        self.m_objects: list[Object] = []     # 관리 중인 오브젝트 리스트.

    # 관리할 오브젝트를 추가합니다.
    def AddObject(self, _newObject: Object) -> None:
        self.m_addObjects.append(_newObject)

    # 관리하는 오브젝트들의 Update()를 실행합니다.
    def Update(self, _deltaTime: float) -> None:
        # 추가할 오브젝트가 있을 경우 관리 중인 리스트에 추가
        if self.m_addObjects:
            self.m_objects.extend(self.m_addObjects)  # 올바른 방법으로 추가
            self.m_addObjects.clear()  # 추가한 후 리스트 비우기

        # 관리 중인 오브젝트가 있을 경우 업데이트 실행
        if self.m_objects:
            self.m_objects.sort(key=lambda obj: obj.renderLayer)  # renderLayer에 따라 정렬
            for obj in self.m_objects:
                obj.Update(_deltaTime)  # 각 오브젝트의 Update 호출

            for obj in self.m_objects:
                obj.LateUpdate(_deltaTime)  # 각 오브젝트의 LateUpdate 호출
        
    # 관리하는 오브젝트들의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        if self.m_objects:
            toRemove: list[Object] = []  # 제거할 오브젝트 리스트
            
            for obj in self.m_objects:
                obj.FixedUpdate(_fixedDeltaTime)  # 각 오브젝트의 FixedUpdate 호출
                if obj.isDestroied:  # 오브젝트가 파괴된 경우
                    toRemove.append(obj)  # 제거할 리스트에 추가

            for obj in toRemove:
                self.m_objects.remove(obj)  # 파괴된 오브젝트 제거

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if self.m_objects:
            for obj in self.m_objects:
                obj.Render()  # 각 오브젝트의 Render 호출
                obj.RenderDebug()  # 각 오브젝트의 RenderDebug 호출