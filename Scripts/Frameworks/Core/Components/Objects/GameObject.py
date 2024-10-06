from Core.Components.Objects.Object import Object

# 게임 내 모든 오브젝트의 베이스 클래스.
class GameObject(Object):
    def __init__(self):
        super().__init__()

        from Core.Components.Component import ComponentManager
        from Core.Components.Transform.Transform import Transform
        from Core.Components.Renderer.SpriteRenderer import SpriteRenderer

        self.name: str = "Game Object"
        self._componentManager: ComponentManager = ComponentManager() # Component Manager 선언 및 초기화
        self._componentManager.AddComponent(Transform(self))          # Transform Add
        self._componentManager.AddComponent(SpriteRenderer(self))     # SpriteRenderer Add
        self.isActive: bool = True

    # 해당 플레이어의 Transform
    @property
    def transform(self) -> 'Transform':
        from Core.Components.Transform.Transform import Transform

        component = self._componentManager.GetComponent(Transform)
        if isinstance(component, Transform):
            return component
        raise TypeError(f"[Oops!] 캐스팅을 시도했으나, 이루어지지 않았습니다. 캐스팅 대상은 {str(component)}였습니다.")

    # 해당 오브젝트의 Sprite Renderer
    @property
    def spriteRenderer(self) -> 'SpriteRenderer':
        from Core.Components.Renderer.SpriteRenderer import SpriteRenderer

        component = self._componentManager.GetComponent(SpriteRenderer)
        if isinstance(component, SpriteRenderer):
            return component
        raise TypeError(f"[Oops!] 캐스팅을 시도했으나, 이루어지지 않았습니다. 캐스팅 대상은 {str(component)}였습니다.")

    # 해당 오브젝트가 'Game Object Manager'에 추가될 때 실행됩니다.
    def Start(self) -> None:
        pass

    # 매 프레임마다 실행됩니다.
    # ※ 게임 오브젝트 상속 받은 클래스 작성할 때 반드시 부모 FixedUpdate() 호출할 것!
    def Update(self, _deltaTime: float) -> None:
        self._componentManager.Update(_deltaTime)

    # 매 고정 프레임마다 실행됩니다.
    # ※ 게임 오브젝트 상속 받은 클래스 작성할 때 반드시 부모 FixedUpdate() 호출할 것!
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        self._componentManager.FixedUpdate(_fixedDeltaTime)

    # Update() 이후 실행됩니다.
    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    # 해당 오브젝트가 파괴되었을 때 실행됩니다.
    def Destroy(self):
        pass

    def Render(self):
        pass

