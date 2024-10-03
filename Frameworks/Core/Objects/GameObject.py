from abc import ABC, abstractmethod
from typing import final

from Core.Objects.Sprite import ELayerLevel
from Core.Utilities.Mathematics import Vector2

# 게임 내 사용되는 모든 오브젝트의 베이스 클래스.
class GameObject(ABC):
    def __init__(self) -> None:
        self.position: Vector2      = Vector2()     # 오브젝트 위치.
        self.scale: Vector2         = Vector2()     # 오브젝트 크기
        self.rotate: float          = 0             # 오브젝트 회전 각도.

        self.isActive: bool         = True          # 오브젝트 활성화 여부.
        self.isDestroy: bool        = False         # 오브젝트 파괴 여부.

    # -----------[추상 메서드]-------------- #
    @abstractmethod
    def Start(self) -> None:
        pass

    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

@final
class ObjectManager:
    def __init__(self) -> None:
        self.m_addObjects: list[GameObject] = []  # 추가할 오브젝트 리스트.
        self.m_objects: dict[ELayerLevel:list[GameObject]] = {}  # 관리 중인 오브젝트 리스트.

    # 관리할 오브젝트를 추가합니다.
    def AddObject(self, _newObject: GameObject) -> None:
        self.m_addObjects.append(_newObject)

    # 관리 중인 모든 오브젝트를 삭제합니다.
    def ClearObjects(self) -> None:
        if len(self.m_addObjects) > 0:
            self.m_addObjects.clear()

        if len(self.m_objects) > 0:
            self.m_objects.clear()

    # 관리하는 오브젝트들의 Update()를 실행합니다.
    def Update(self, _deltaTime: float) -> None:
        # 추가할 오브젝트가 있을 경우 추가합니다.
        if len(self.m_addObjects) > 0:
            for layerLevel in self.m_addObjects:
                if layerLevel.sprite.renderInfo.layerLevel not in self.m_objects.keys():
                    self.m_objects[layerLevel.sprite.renderInfo.layerLevel] = []

                self.m_objects[layerLevel.sprite.renderInfo.layerLevel].append(layerLevel)

            self.m_addObjects.clear()

        # 관리 중인 오브젝트가 있을 경우 업데이트 실행
        if len(self.m_objects) > 0:
            for layerLevel in self.m_objects:
                for object in self.m_objects[layerLevel]:
                    if object.isActive:
                        object.Update(_deltaTime)
                        object.sprite.Update(_deltaTime)

            for layerLevel in self.m_objects:
                for object in self.m_objects[layerLevel]:
                    if object.isActive:
                        object.LateUpdate(_deltaTime)

    # 관리하는 오브젝트들의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        if len(self.m_objects) > 0:
            toRemove: list[GameObject] = []  # 제거할 오브젝트 리스트
            for layerLevel in self.m_objects:
                for object in self.m_objects[layerLevel]:
                    object.FixedUpdate(_fixedDeltaTime)
                    if object.isActive and object.isDestroy:
                        toRemove.append(object)

            if len(toRemove) > 0:
                for obj in toRemove:
                    self.m_objects.remove(obj)

        if len(self.m_objects) > 0:
            for objects in self.m_objects.values():
                for object in objects:
                    if object.collisionLayer == 0:
                        continue

                for object2 in objects:
                    if object == object2:
                        continue

                    if (object == object2 and
                            object.collisionLayer != object2.collisionLayer):
                        continue

                    if (object.collider != None and
                            object2.collider != None):
                        if object.collider.IsCollision(object2.collider) and object2.IsCollision(object.collider):
                            if not object.collider.useTrigger:
                                object.OnCollision(object2.collider)
                            if not object2.collider.useTrigger:
                                object2.OnCollision(object.collider)

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if len(self.m_objects) > 0:
            for layerLevel in sorted(self.m_objects.keys(), key=lambda x: x.value):
                for object in self.m_objects[layerLevel]:
                    if object.isActive:
                        object.Render()  # 각 오브젝트의 Render 호출
                        object.RenderDebug()  # 각 오브젝트의 RenderDebug 호출