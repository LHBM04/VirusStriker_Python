from typing import Dict

from Core.Components.Component import Component
from Core.Components.Animation.Animation import Animation
from Core.Components.GameObject import GameObject

# 스프라이트를 교체하는 등의 애니메이션을 구현합니다.
class Animator(Component):
    def __init__(self, _owner: GameObject, _animator: 'Animator'):
        super().__init__(_owner, )
        self.__animator: 'Animator' = _animator
        self.__animations: Dict[str : Animation] = {}  # 해당 스프라이트의 텍스쳐들
        self.__currentState: str = ""
        self.__animationCount: int = 0

    def OnUpdate(self, _deltaTime: float):
        pass

    def OnRender(self):
        pass