from abc import ABC, abstractmethod
from typing import final
from enum import Enum

from sdl2 import *
from sdl2dll import *

from Core.Sprite import *
from Core.Actors.Object import *
from Utilities.Vector2 import *
from Utilities.Vector3 import *

# AABB형 콜리전 바디
class Collider2D:
    # 충돌 검사를 위한 열거형.
    # 필요한 게 있을 때마다 추가하여 쓰도록 하자
    class ETag(Enum):
        NONE    = 0 # 더미 태그(기본).
        HARMFUL = 1 # 플레이어에게 해로운 오브젝트의 태그
        LETHAL  = 2 # 플레이어에게 치명적인(즉사) 오브젝트의 태그

    def __init__(self, _owner: 'Object',  _min: Vector2, _max: Vector2) -> None:
        self.owner: 'Object' = _owner
        self.min: Vector2    = _min
        self.max: Vector2    = _max

# 충돌 검사
def IsCollision(_lhs: Collider2D, _rhs: Collider2D) -> bool:
    # AABB 검사
    min1: Vector2 = _lhs.owner.position + _lhs.min
    max1: Vector2 = _lhs.owner.position + _lhs.max
    min2: Vector2 = _rhs.owner.position + _rhs.min
    max2: Vector2 = _rhs.owner.position + _rhs.max

    if (min1.x > max2.x and max1.x > min2.x and 
        min1.y > max2.y and max1.y > min2.y):
        return True

    return False

# TODO: 트리거 판정도 만들기
def IsTrigger(_lhs: Collider2D, _rhs: Collider2D) -> bool:
    pass

# 게임 내 사용되는 모든 오브젝트의 베이스 클래스.
class Object(ABC):
    def __init__(self) -> None:
        self.position: Vector2 = Vector2()                                  # 오브젝트 위치.
        
        self.sprite: Sprite             = None                              # 오브젝트 스프라이트.
        self.spriteInfo: SpriteInfo     = None                              # 오브젝트 스프라이트 정보.
        self.renderLayer: int           = 0                                 # 오브젝트의 렌더링 순서.
        
        self.collisionLayer: Collider2D.ELayer  = Collider2D.ETag.NONE      # 오브젝트의 충돌 레이어.
        self.colisionTag: Collider2D.ETag       = Collider2D.ETag.NONE      # 오브젝트의 충돌 태그.
        self.bodies: list[Collider2D]           = []                        # 오브젝트의 콜라이더 리스트.
        
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
    def OnCollision(self, _collider: Collider2D) -> None:
        pass
    
    @abstractmethod
    def OnTrigger(self, _collider: Collider2D) -> None:
        pass

    @abstractmethod
    def Render(self) -> None:
        pass

    def RenderDebug(self) -> None:
        for body in self.bodies:
            if not (body.min != Vector2(0, 0) and body.max != Vector2(0, 0)):
                # 바디의 위치 계산
                minp: Vector2 = body.min + body.owner.position
                maxp: Vector2 = body.max + body.owner.position
        
                # 히트박스의 크기 계산
                width = maxp.x - minp.x
                height = maxp.y - minp.y
        
                min_x = minp.x - (width / 2)
                min_y = minp.y - (height / 2)
        
                SDL_SetRenderDrawColor(pico2d.renderer, 255, 255, 0, 255)  # 색상 설정
                SDL_RenderDrawRect(pico2d.renderer, SDL_Rect(int(min_x), int(min_y), int(width), int(height)))  # rect를 참조로 전달


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

            if len(toRemove) > 0:
                for obj in toRemove:
                    self.m_objects.remove(obj)

        if len(self.m_objects) > 0:
            for iter in self.m_objects:
                if iter.collisionLayer == 0:
                    continue

                for iter2 in self.m_objects:
                    if iter == iter2 and iter.collisionLayer != iter2.collisionLayer:
                        continue

                    for body in iter.bodies:
                        for body2 in iter.bodies:
                            if IsCollision(body, body2):
                                iter.OnCollision(body2)
                                iter2.OnCollision(body)

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if len(self.m_objects) > 0:
            for obj in self.m_objects:
                obj.Render()  # 각 오브젝트의 Render 호출
                obj.RenderDebug()  # 각 오브젝트의 RenderDebug 호출