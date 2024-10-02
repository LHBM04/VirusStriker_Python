import numpy as np
from pico2d import *

from Frameworks.Core.Utilities.Mathematics.Vector2 import Vector2

class Camera:
    def __init__(self):
        self.position: Vector2  = Vector2(0.0, 0.0)
        self.rotation: float    = 0.0
        self.scale: float       = 5.0

    def ScreenToWorld(self, _screenPos: Vector2) -> Vector2:
        hw = get_canvas_width() / 2
        hh = get_canvas_height() / 2

        v = _screenPos - Vector2(hw, hh)
        v = self.position + v * (self.scale / hh)

        return v

    def WorldToScreen(self, _worldPos: Vector2, _rotate: int = 1) -> Vector2:
        hw = get_canvas_width() / 2
        hh = get_canvas_height() / 2

        v = _worldPos - self.position

        if self.rotation != 0:
            radian = -np.radians(self.rotation * _rotate)
            v = Vector2(v.x * np.cos(radian) - v.y * np.sin(radian), v.x * np.sin(radian) - v.y * np.cos(radian))

        return v

    def RotateScreen(self, _worldPos: float, rotateFactor: int = 1) -> float:
        return _worldPos - self.rotation * rotateFactor

    def RescaleScreen(self, _worldSize: Vector2):
        hh = get_canvas_height() / 2
        return _worldSize * (hh / self.scale)

class CameraController:
    def __init__(self):
        pass