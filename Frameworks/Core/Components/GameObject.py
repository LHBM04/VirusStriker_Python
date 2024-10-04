from abc import ABCMeta, abstractmethod
from typing import final, List, Dict

from Frameworks.Core.Components.Component import ComponentManager
from Frameworks.Core.Components.Transform import Transform
from Frameworks.Core.Components.SpriteRenderer import SpriteRenderer, ESortingLayer

# 게임 내 모든 오브젝트의 베이스 클래스.
class GameObject(metaclass = ABCMeta):
    def __init__(self):
        self.name: str = "Game Object"
        self._componentManager: ComponentManager = ComponentManager() # Component Manager 선언 및 초기화
        self._componentManager.AddComponent(Transform(self))          # Transform Add
        self._componentManager.AddComponent(SpriteRenderer(self))     # SpriteRenderer Add

    # 해당 플레이어의 Transform
    @property
    def transform(self) -> Transform:
        component = self._componentManager.GetComponent(Transform)
        if isinstance(component, Transform):
            return component
        raise TypeError(f"[Oops!] 캐스팅을 시도했으나, 이루어지지 않았습니다. 캐스팅 대상은 {str(component)}였습니다.")

    # 해당 오브젝트의 Sprite Renderer
    @property
    def spriteRenderer(self) -> SpriteRenderer:
        component = self._componentManager.GetComponent(SpriteRenderer)
        if isinstance(component, SpriteRenderer):
            return component
        raise TypeError(f"[Oops!] 캐스팅을 시도했으나, 이루어지지 않았습니다. 캐스팅 대상은 {str(component)}였습니다.")

    # 해당 오브젝트가 'Game Object Manager'에 추가될 때 실행됩니다.
    @abstractmethod
    def Start(self) -> None:
        pass

    # 매 프레임마다 실행됩니다.
    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        self._componentManager.Update(_deltaTime)

    # 매 고정 프레임마다 실행됩니다.
    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self._componentManager.FixedUpdate(_fixedDeltaTime)

    # Update() 이후 실행됩니다.
    @abstractmethod
    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    # 해당 오브젝트가 파괴되었을 때 실행됩니다.
    @abstractmethod
    def Destroy(self):
        pass

# Scene 내에서 사용되는 모든 오브젝트를 관리합니다.
@final
class GameObjectManager:
    def __init__(self) -> None:
        self.m_objects: Dict[ESortingLayer : List[GameObject]]  = {}  # 관리 중인 오브젝트 리스트.
        self.m_addObjects: List[GameObject]                     = []  # 추가할 오브젝트 리스트.

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
            for addObject in self.m_addObjects:
                if addObject.spriteRenderer.sortingLayer not in self.m_objects.keys():
                    self.m_objects[addObject.spriteRenderer.sortingLayer] = []

                self.m_objects[addObject.spriteRenderer.sortingLayer].append(addObject)

            self.m_addObjects.clear()

        if len(self.m_objects) > 0:
            # Update() 실행
            for sortingLayer in ESortingLayer:
                for currentObject in self.m_objects[sortingLayer]:
                    if currentObject.isActive:
                        currentObject.Update(_deltaTime)
                        currentObject.sprite.Update(_deltaTime)

            # LateUpdate() 실행
            for sortingLayer in ESortingLayer:
                for currentObject in self.m_objects[sortingLayer]:
                    if currentObject.isActive:
                        currentObject.LateUpdate(_deltaTime)

    # 관리하는 오브젝트들의 FixedUpdate()를 실행합니다.
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        if len(self.m_objects) > 0:
            toRemove: list[GameObject] = []  # 제거할 오브젝트 리스트
            for sortingLayer in ESortingLayer:
                for currentObject in self.m_objects[sortingLayer]:
                    currentObject.FixedUpdate(_fixedDeltaTime)
                    if (currentObject.isActive and
                        currentObject.isDestroy):
                        toRemove.append(currentObject)

            if len(toRemove) > 0:
                for currentObject in toRemove:
                    self.m_objects[currentObject.spriteRenderer.sortingLayer](currentObject)
        
        # 물리(충돌) 이벤트를 처리합니다.
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
                        if (object.collider.IsCollision(object2.collider) and
                            object2.IsCollision(object.collider)):
                            if not object.collider.__useTrigger:
                                object.OnCollision(object2.collider)
                            if not object2.collider.__useTrigger:
                                object2.OnCollision(object.collider)

    # 관리하는 오브젝트들의 Render()를 실행합니다.
    def Render(self) -> None:
        if len(self.m_objects) > 0:
            for layerLevel in sorted(self.m_objects.keys(), key=lambda x: x.value):
                for object in self.m_objects[layerLevel]:
                    if object.isActive:
                        object.Render()  # 각 오브젝트의 Render 호출
                        object.RenderDebug()  # 각 오브젝트의 RenderDebug 호출
