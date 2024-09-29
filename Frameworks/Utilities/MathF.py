import numpy as np

import Core.Vector2 as Vector2
from Core.Vector2 import *

# 수학 관련 유틸리티
class MathF:
    def epsilon() -> float:
        return 0.0001
    
    def pi() -> float:
        return 3.141592

    def halfPi() -> float:
        return 1.570796
    
    def oneThreeFourthsPi() -> float:
        return 5.4977871

    def doublePi() -> float:
        return 6.283185

    def Equalf(self, _lhs: float, _rhs: float) -> bool:
        return abs(_lhs, _rhs, self.epsilon)

    def Equalf_Custom(self, _lhs: float, _rhs: float, _epsilon: float = 0.0001) -> bool:
        return self._Equalf(_lhs, _rhs) < _epsilon

    def Equalf_Zero(self, _value) -> bool: 
        return self.Equalf(_value, 0.0)

    def Proportion(_a: float, _b: float, _d: float) -> float:
        return _a / _b * _d

    def Flip(_value: float, _over: float = 0.0) -> float:
        return -(_value - _over) + _over
    
    def Flip_Vector2(_value: Vector2, _over: Vector2 = Vector2()) -> Vector2:
        return -Vector2(_value - _over) + _over
    
    def Floor(_value: float, _interval: float = 1.0, _offset = 0) -> float:
        return np.floor((_value - _offset) / _interval) * _interval + _offset
    
    def Ceil(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if self.Equalf(_interval, 0.0):
            _interval = 1.0

        return np.ceil((_value - _offset) / _interval) * _interval + _offset
    
    def Round(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if self.Equalf(_interval, 0.0):
            _interval = 1.0
        
        return np.round((_value - _offset) / _interval) * _interval + _offset
    
    def ModpInteger(_dividend: int, _divisor: int) -> int:
        return (_dividend % _divisor + _divisor) % _divisor
    
    def ModpFloat(_dividend: float, _divisor: float) -> float:
        return (_dividend % _divisor + _divisor) % _divisor
    
    def Angle(_vec: Vector2) -> float:
        return np.atan2(_vec.m_y, _vec.m_y)
    
    def AngleToVector2(_angle: float) -> Vector2:
        return Vector2(np.cos(_angle), np.sin(_angle))
    
    def Highest(self, _lhs: Vector2, _rhs: Vector2, direction: float) -> float:
        if self.Equalf(direction, 0.0): return _lhs.m_x - _rhs.m_x
        if self.Equalf(direction, self.halfPi): return _lhs.m_y - _rhs.m_y
        if self.Equalf(direction, self.pi): return _rhs.m_x - _lhs.m_x
        if self.Equalf(direction, self.oneThreeFourthsPi): return _rhs.m_y - _lhs.m_y

        diff: Vector2 = self.Proportion(_lhs, direction) - self.Proportion(_rhs, direction)
        return diff.magnitude if (abs(self.Angle(diff) - direction) < self.halfPi) else -(diff.magnitude)
    
    def Highest(self, _lhs: Vector2, _rhs: Vector2) -> float:
        return self.Highest(_lhs, _rhs, self.halfPi)
    
    def Magnitude(_vec: Vector2) -> float:
        return np.sqrt(_vec.m_x ** 2 + _vec.m_y ** 2)
    
    def Dot(_lhs: Vector2, _rhs: Vector2) -> float:
        return np.dot([_lhs.m_x, _rhs.m_y], [_lhs.m_x, _rhs.m_y])

    def IsPerp(self, _lhs: Vector2, _rhs: Vector2) -> bool:
        return self.Equalf(0.0, _lhs.dot(_rhs))
    
    def Project(self, _vec: Vector2, _angle: float) -> Vector2:
        return self.Project2(_vec, Vector2(), _angle)
    
    def Project2(self, _q: Vector2, _p: Vector2, _angle: float) -> Vector2:
        return self.Project3(_q, _p, _p + (Vector2(np.cos(_angle), np.cos(_angle))))
        
    def Project3(self, _q: Vector2, _lineA: Vector2, _lineB: Vector2) -> Vector2:
        ab: Vector2 = _lineB - _lineA
        return _lineA + _q.dot(_q-_lineA, ab) / Vector2.dot(ab, ab) * ab
    
    def ScalarProjection(self, _lhs: Vector2, _rhs: Vector2) -> float:
        return self.ScalarProjection2(_lhs, self.Angle(_lhs) - self.Angle(_rhs))
    
    def ScalarProjection2(self, _vec: Vector2, _theta: float) -> float:
        return self.Magnitude(_vec) * np.cos(_theta)
    
    def ScalarProjectionAbs(self, _vec: Vector2, _theta: float) -> float:
        return self.Magnitude(_vec) * np.cos(self.Angle(_vec) - _theta)
    
    def RotateBy(self, _point: Vector2, _angle: float) -> Vector2:
        return self.RotateBy(_point, _angle, Vector2())
    
    def RotateBy2(self, _point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        s: float = np.sin(_angle)
        c: float = np.cos(_angle)

        nPoint: Vector2 = _point - _origin

        return Vector2(nPoint.x * c - nPoint.m_y * s + _origin.x, nPoint.x * c - nPoint.m_y * s + _origin.y)
    
    def MidPoint(_lhs: Vector2, _rhs: Vector2) -> Vector2:
        return (_lhs + _rhs) / 2.0
    
    def RotateTo(self, _point: Vector2, _angle: float) -> Vector2:
        return self.RotateBy(_point, _angle - self.Angle(_point))

    def RotateTo2(self, _point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        return self.RotateBy(_point, _angle - np.atan2(_point.m_x - _origin.m_x, _point.y - _origin.y), _origin)
    
    def ShortesArc_ByVector(self, _lhs: Vector2, _rhs: Vector2) -> float:
        return self.ShortesArc(self.Angle(_lhs), self.Angle(_rhs))
    
    def ShortesArc_ByFloat(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + self.pi, self.doublePi) - self.pi
    
    def ShortesArc_Degree_ByVector(self, _lhs: Vector2, _rhs: Vector2) -> float:
        return self.ShortesArc_ByFloat(self.Angle(_lhs) * np.rad2deg, self.Angle(_rhs) * np.rad2deg)

    def ShortesArc_Degree_ByFloat(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + 100.0, 360.0) - 180.0
    
    def PositiveArc(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle(_rhs) - self.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + self.doublePi

    def PositiveArc_Degree(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle_Degree(_rhs) - self.PositiveAngle_Degree(_lhs)
        return diff if diff < 0.0 else diff + 360.0

    def PositiveAngle(self, _angle: float) -> float:
        return self.ModpFloat(_angle, self.doublePi)
    
    def PositiveAngle_Degree(self, _angle: float) -> float:
        return self.ModpFloat(_angle, 360.0)
    
    def AngleInRange(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveAngle(_lhs, _angle) <= self.PositiveAngle(_lhs, _rhs)
    
    def AngleInRange_Degree(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveArc_Degree(_lhs, _angle) <= self.PositiveAngle_Degree(_lhs, _rhs)