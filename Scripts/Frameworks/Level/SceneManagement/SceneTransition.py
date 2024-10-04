from typing import Callable

from Core.Components.GameObject import GameObject
from Core.System import SystemManager
from Core.Utilities.ResourceManagement import ResourceManager
from Core.Utilities.Mathematics.Vector2 import Vector2
from Core.Components.SpriteRenderer import Color

# Scene 간의 전환 사이 로딩 애니메이션을 구현합니다.
class SceneTransition(GameObject):
    def __init__(self):
        super().__init__()
        
        # 이름 초기화
        self.name = "Scene Transition"

        # Transfrom 초기화
        self.transform.position = Vector2(SystemManager().windowWidth / 2, SystemManager().windowHeight / 2)
        self.transform.scale = Vector2(SystemManager().windowWidth, SystemManager().windowHeight)
        
        # Sprite Renderer 초기화
        self.spriteRenderer.sprite = ResourceManager().GetSprite(r"Resources\Sprites\Backgrounds\Sprite_Background_Initialize.png")
        self.spriteRenderer.color = Color(255, 255, 255, 0)

        self.__nextScene: str = ""
        self.__transitionEvent: Callable = None
        self.__fadeSpeed: float = 200.0

    def Update(self, _deltaTime: float) -> None:
        from Level.SceneManagement.SceneManager import SceneManager

        super().Update(_deltaTime)

        # 이동할 Scene이 없다면 메서드를 종료합니다.
        if (self.__nextScene is not None and
            self.__nextScene != ""):
            self.spriteRenderer.color.a += _deltaTime * self.__fadeSpeed
            if self.spriteRenderer.color.a >= Color.MaxValue():
                self.spriteRenderer.color.a = Color.MaxValue()

            self.__transitionEvent()

            self.__nextScene = ""
            self.__transitionEvent = None

            SceneManager().isResetDeltaTime = True
        else:
            self.spriteRenderer.color.a -= _deltaTime * self.__fadeSpeed
            if self.spriteRenderer.color.a <= Color.MinValue():
                self.spriteRenderer.color.a = Color.MinValue()
                self.isActive = False

    def GoTo(self, _sceneName: str, _callback: Callable):
        self.__nextScene = _sceneName
        self.__transitionEvent = _callback

        self.isActive = True
        self.spriteRenderer.color.a = 0
        self.Render()

