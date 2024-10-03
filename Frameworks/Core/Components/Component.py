from abc import ABC

from Core.Components.GameObject import GameObject

# 모든 컴포넌트의 베이스 클래스
class Component(ABC):
    def __init__(self, _owner: 'GameObject',):
        self.owner: 'GameObject' = _owner