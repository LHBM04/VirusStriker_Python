from Core.Object import *

class Entity(Object):
    def __init__(self) -> None:
        super().__init__()

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

    def Render(self) -> None:
        super().Render()
        self.RenderDebug()

    @final
    def RenderDebug(self) -> None:
        if self.collider == None:
            return
        
        if (self.collider.min != Vector2.Zero() and 
            self.collider.max != Vector2.Zero()):
                minp: Vector2 = self.collider.min + self.collider.owner.position
                maxp: Vector2 = self.collider.max + self.collider.owner.position
        
                draw_rectangle(minp.x, minp.y, maxp.x, maxp.y)