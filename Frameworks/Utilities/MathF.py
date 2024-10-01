from typing import final
import numpy as np

import Utilities.Vector2 as Vector2

# 수학 관련 유틸리티
@final
class MathF:
    @staticmethod
    def epsilon() -> float:
        return 0.0001
    
    @staticmethod
    def pi() -> float:
        return 3.141592

    @staticmethod
    def halfPi() -> float:
        return 1.570796
    
    @staticmethod
    def oneThreeFourthsPi() -> float:
        return 5.4977871

    @staticmethod
    def doublePi() -> float:
        return 6.283185

    @staticmethod
    def Equalf(_lhs: float, _rhs: float) -> bool:
        return np.abs(_lhs - _rhs) < MathF.epsilon()

    @staticmethod
    def Equalf_Custom(_lhs: float, _rhs: float, _epsilon: float = 0.0001) -> bool:
        return np.abs(_lhs - _rhs) < _epsilon

    @staticmethod
    def Equalf_Zero(_value) -> bool: 
        return MathF.Equalf(_value, 0.0)

    @staticmethod
    def Proportion(_a: float, _b: float, _d: float) -> float:
        return _a / _b * _d

    @staticmethod
    def Flip(_value: float, _over: float = 0.0) -> float:
        return -(_value - _over) + _over
    
    @staticmethod
    def Flip_Vector2(_value: Vector2, _over: Vector2 = None) -> Vector2:
        if _over is None:
            _over = Vector2(0.0, 0.0)

        return -(_value - _over) + _over
    
    @staticmethod
    def Floor(_value: float, _interval: float = 1.0, _offset = 0) -> float:
        return np.floor((_value - _offset) / _interval) * _interval + _offset
    
    @staticmethod
    def Ceil(_value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if MathF.Equalf(_interval, 0.0):
            _interval = 1.0

        return np.ceil((_value - _offset) / _interval) * _interval + _offset
    
    @staticmethod
    def Round(_value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if MathF.Equalf(_interval, 0.0):
            _interval = 1.0
        
        return np.round((_value - _offset) / _interval) * _interval + _offset
    
    @staticmethod
    def ModpInteger(_dividend: int, _divisor: int) -> int:
        return (_dividend % _divisor + _divisor) % _divisor
    
    @staticmethod
    def ModpFloat(_dividend: float, _divisor: float) -> float:
        return (_dividend % _divisor + _divisor) % _divisor
    
    @staticmethod
    def Angle(_vec: Vector2) -> float:
        return np.atan2(_vec.m_y, _vec.m_x)
    
    @staticmethod
    def AngleToVector2(_angle: float) -> Vector2:
        return Vector2(np.cos(_angle), np.sin(_angle))
    
    @staticmethod
    def Highest(_lhs: Vector2, _rhs: Vector2, direction: float) -> float:
        if MathF.Equalf(direction, 0.0): return _lhs.m_x - _rhs.m_x
        if MathF.Equalf(direction, MathF.halfPi): return _lhs.m_y - _rhs.m_y
        if MathF.Equalf(direction, MathF.pi): return _rhs.m_x - _lhs.m_x
        if MathF.Equalf(direction, MathF.oneThreeFourthsPi): return _rhs.m_y - _lhs.m_y

        diff: Vector2 = MathF.Proportion(_lhs, direction) - MathF.Proportion(_rhs, direction)
        return diff.magnitude if (abs(MathF.Angle(diff) - direction) < MathF.halfPi) else -(diff.magnitude)
    
    @staticmethod
    def Highest_V2(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.Highest(_lhs, _rhs, MathF.halfPi)
    
    @staticmethod
    def Magnitude(_vec: Vector2) -> float:
        return np.sqrt(_vec.m_x ** 2 + _vec.m_y ** 2)
    
    @staticmethod
    def Dot(_lhs: Vector2, _rhs: Vector2) -> float:
        return np.dot([_lhs.m_x, _lhs.m_y], [_rhs.m_x, _rhs.m_y])

    @staticmethod
    def IsPerp(_lhs: Vector2, _rhs: Vector2) -> bool:
        return MathF.Equalf(0.0, MathF.Dot(_lhs, _rhs))
    
    @staticmethod
    def Project(_vec: Vector2, _angle: float) -> Vector2:
        return MathF.Project2(_vec, Vector2(0.0, 0.0), _angle)
    
    @staticmethod
    def Project2(_q: Vector2, _p: Vector2, _angle: float) -> Vector2:
        return MathF.Project3(_q, _p, _p + Vector2(np.cos(_angle), np.sin(_angle)))
        
    @staticmethod
    def Project3(_q: Vector2, _lineA: Vector2, _lineB: Vector2) -> Vector2:
        ab: Vector2 = _lineB - _lineA
        return _lineA + _q.dot(_q-_lineA, ab) / MathF.Dot(ab, ab) * ab
    
    @staticmethod
    def ScalarProjection(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ScalarProjection2(_lhs, MathF.Angle(_lhs) - MathF.Angle(_rhs))
    
    @staticmethod
    def ScalarProjection2(_vec: Vector2, _theta: float) -> float:
        return MathF.Magnitude(_vec) * np.cos(_theta)
    
    @staticmethod
    def ScalarProjectionAbs(_vec: Vector2, _theta: float) -> float:
        return MathF.Magnitude(_vec) * np.cos(MathF.Angle(_vec) - _theta)
    
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy2(_point, _angle, Vector2(0.0, 0.0))
    
    @staticmethod
    def RotateBy2(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        s: float = np.sin(_angle)
        c: float = np.cos(_angle)

        nPoint: Vector2 = _point - _origin

        return Vector2(nPoint.m_x * c - nPoint.m_y * s + _origin.m_x, nPoint.m_x * s + nPoint.m_y * c + _origin.m_y)
    
    @staticmethod
    def MidPoint(_lhs: Vector2, _rhs: Vector2) -> Vector2:
        return (_lhs + _rhs) / 2.0
    
    @staticmethod
    def RotateTo(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy(_point, _angle - MathF.Angle(_point))

    @staticmethod
    def RotateTo2(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        return MathF.RotateBy(_point, _angle - np.atan2(_point.m_y - _origin.m_y, _point.m_x - _origin.m_x), _origin)
    
    @staticmethod
    def ShortesArc_ByVector(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc(MathF.Angle(_lhs), MathF.Angle(_rhs))
    
    @staticmethod
    def ShortesArc_ByFloat(_lhs: float, _rhs: float) -> float:
        return MathF.ModpFloat(_rhs - _lhs + MathF.pi, MathF.doublePi) - MathF.pi
    
    @staticmethod
    def ShortesArc_Degree_ByVector(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc_ByFloat(MathF.Angle(_lhs) * np.rad2deg(1), MathF.Angle(_rhs) * np.rad2deg(1))

    @staticmethod
    def ShortesArc_Degree_ByFloat(_lhs: float, _rhs: float) -> float:
        return MathF.ModpFloat(_rhs - _lhs + 100.0, 360.0) - 180.0
    
    @staticmethod
    def PositiveArc(_lhs: float, _rhs: float) -> float:
        diff: float = MathF.PositiveAngle(_rhs) - MathF.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + MathF.doublePi

    @staticmethod
    def PositiveArc_Degree(_lhs: float, _rhs: float) -> float:
        diff: float = MathF.PositiveAngle_Degree(_rhs) - MathF.PositiveAngle_Degree(_lhs)
        return diff if diff < 0.0 else diff + 360.0

    @staticmethod
    def PositiveAngle(_angle: float) -> float:
        return MathF.ModpFloat(_angle, MathF.doublePi)
    
    @staticmethod
    def PositiveAngle_Degree(_angle: float) -> float:
        return MathF.ModpFloat(_angle, 360.0)
    
    @staticmethod
    def AngleInRange(_angle: float, _lhs: float, _rhs: float) -> bool:
        return MathF.PositiveAngle(_lhs) <= MathF.PositiveAngle(_rhs)
    
    @staticmethod
    def AngleInRange_Degree(_angle: float, _lhs: float, _rhs: float) -> bool:
        return MathF.PositiveArc_Degree(_lhs, _angle) <= MathF.PositiveAngle_Degree(_rhs)