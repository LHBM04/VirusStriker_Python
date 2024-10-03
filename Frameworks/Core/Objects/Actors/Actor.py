from typing import final

from pico2d import *

from Core.Objects import Collider2D, GameObject
from Core.Utilities.Mathematics import Vector2

class Actor(GameObject):
    def __init__(self):
        super.__init__()

        self.collider: Collider2D = None                  # 오브젝트 콜라이더
        self.collisionLayer: Collider2D.ELayer  = Collider2D.EColliderTag.NONE  # 오브젝트의 충돌 레이어.
        self.colisionTag: Collider2D.EColliderTag       = Collider2D.EColliderTag.NONE  # 오브젝트의 충돌 태그.

    def OnCollisionEnter(self, _collider: Collider2D) -> None:
        pass

    def OnCollisionExit(self, _collider: Collider2D) -> None:
        pass

    def OnTriggerEnter(self, _collider: Collider2D) -> None:
        pass

    def OnTriggerStay(self, _collider: Collider2D) -> None:
        pass

    def OnTriggerExit(self, _collider: Collider2D) -> None:
        pass

    @final
    def RenderDebug(self) -> None:
        if self.collider == None:
            return

        if self.collider.min != Vector2.Zero() and self.collider.max != Vector2.Zero():
            # 바디의 위치 계산
            minp: Vector2 = self.collider.min + self.collider.owner.position
            maxp: Vector2 = self.collider.max + self.collider.owner.position

            draw_rectangle(minp.x, minp.y, maxp.x, maxp.y)