from logging import fatal
from typing import final
from typing import List

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject
from Core.Utilities.Mathematics import Vector2

# 오브젝트의 위치, 크기, 회전값 등을 저장하는 컴포넌트
@final
class Transform(Component):
    def __init__(self, _owner: 'GameObject'):
        super().__init__(_owner)

        self.position: 'Vector2'            = Vector2(0.0, 0.0) # 현재 포지션
        self.scale: 'Vector2'               = Vector2(0.0, 0.0) # 현재 크기
        self.rotation: (bool, bool, float)  = (False, False, 0.0)     # 현재 회전값. (X, Y축은 Boolean.)

        self.parent: 'Transform'            = None                    # 부모 트랜스폼
        self.children: List['Transform']    = []                      # 자식 트랜스폼
