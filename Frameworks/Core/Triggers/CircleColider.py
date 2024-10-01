from Frameworks.Core.Objects.Actors.Actor import Actor
from Frameworks.Core.Triggers.Collider2D import Collider2D

# 원형 Collider2D
class CircleCollider2D(Collider2D):
    def __init__(self, _owner: Actor, _radius: float) -> None:
        super().__init__(_owner)
        self.radius: float = _radius

    def IsCollision(self, _other: 'Collider2D') -> bool:
        pass

    def IsTrigger(self, _other: 'Collider2D') -> bool:
        # 트리거 상태 검사 (충돌 검사와 비슷하지만 트리거 이벤트 처리 추가)
        if self.IsCollision(_other):
            if not self.isTrigger:
                self.OnTriggerEnter(_other)
            self.isTrigger = True
            self.OnTriggerStay(_other)
        else:
            if self.isTrigger:
                self.OnTriggerExit(_other)
            self.isTrigger = False
