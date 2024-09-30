from abc import ABC, abstractmethod
from typing import final

from pygame import *

from Core.Sprite import *
from Core.Actors.CollisionSystem import *
from Utilities.Vector2 import *
from Utilities.Vector3 import *

# 게임 내 사용되는 모든 오브젝트의 베이스 클래스.
class Object(ABC):
    def __init__(self) -> None:
        self.position: Vector2 = Vector2()                                  # 오브젝트 위치.
        
        self.sprite: Sprite             = None                              # 오브젝트 스프라이트.
        self.spriteInfo: SpriteInfo     = None                              # 오브젝트 스프라이트 정보.
        self.renderLayer: int           = 0                                 # 오브젝트의 렌더링 순서.
        
        self.collisionLayer: int             = 0                            # 오브젝트의 충돌 레이어.
        self.colisionTag: Collider2D.ETag    = Collider2D.ETag.NONE         # 오브젝트의 충돌 태그.
        self.bodies: list[Collider2D]        = []                           # 오브젝트의 콜라이더 리스트.
        
        self.isDestroy: bool = False                                        # 오브젝트 파괴 여부.

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
    def OnCollision(self, _colider: Collider2D) -> None:
        pass
    
    @abstractmethod
    def OnTrigger(self, _colider: Collider2D) -> None:
        pass

    @abstractmethod
    def Render(self) -> None:
        pass

    def RenderDebug(self) -> None:
        for body in self.bodies:
            if body.min != Vector2.Zero() and body.max != Vector2.Zero():
                minp: Vector2 = body.min + body.owner.position
                maxp: Vector2 = body.max + body.owner.position

                draw_rectangle(minp.x, minp.y, maxp.x, maxp.y)

# 오브젝트의 상태를 감시하고, 관리하는 매니저.
@ final
class ObjectManager:
    def __init__(self) -> None:
        self.m_addObjects: list[Object] = []  # 추가할 오브젝트 리스트.
        self.m_objects: list[Object] = []     # 관리 중인 오브젝트 리스트.

    # 관리할 오브젝트를 추가합니다.
    def AddObject(self, _newObject: Object) -> None:
        self.m_addObjects.append(_newObject)

    # 관리 중인 모든 오브젝트를 삭제합니다.
    def ClearObjects(self) -> None:
        if len(self.m_addObjects) > 0:
            self.m_addObjects.clear()

        if len(self.m_objects) > 0:
            self.m_objects.clear()

    # 관리하는 오브젝트들의 Update()를 실행합니다.
    def Update(self, _deltaTime: float) -> None:
        if len(self.m_addObjects) > 0:
            self.m_objects.extend(self.m_addObjects) 
            self.m_addObjects.clear() 

        # 관리 중인 오브젝트가 있을 경우 업데이트 실행
        if len(self.m_objects) > 0:
            self.m_objects.sort(key=lambda obj: obj.renderLayer)  
            for obj in self.m_objects:
                obj.Update(_deltaTime)
                obj.sprite.Update(_deltaTime)

            for obj in self.m_objects:
                obj.LateUpdate(_deltaTime)
        
    # 관리하는 오브젝트들의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        if len(self.m_objects) > 0:
            toRemove: list[Object] = []  # 제거할 오브젝트 리스트
            
            for obj in self.m_objects:
                obj.FixedUpdate(_fixedDeltaTime) 
                if obj.isDestroy: 
                    toRemove.append(obj) 

            for obj in toRemove:
                self.m_objects.remove(obj)
                del obj

        for object in self.m_objects:
            if object.collisionLayer == 0: 
                continue
            
            for object2 in self.m_objects:
                if object.collisionLayer != object2.collisionLayer: 
                    continue

                for body in object.bodies:
                    for body2 in object2.bodies:
                        if IsCollision(body, body2):
                            object.OnCollision(object2)
                            object2.OnCollision(object)

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if len(self.m_objects) > 0:
            for obj in self.m_objects:
                obj.Render()  # 각 오브젝트의 Render 호출
                obj.RenderDebug()  # 각 오브젝트의 RenderDebug 호출