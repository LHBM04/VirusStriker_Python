from typing import final

from multipledispatch import dispatch
from numpy import abs, atan2, ceil, cos, deg2rad, dot, floor, rad2deg, sin, sqrt, tan

from Core.Utilities.Mathematics.Vector2 import Vector2

@final
class MethVec:
    @staticmethod
    def Magnitude(_vec: Vector2) -> float:
        return sqrt(_vec.m_x ** 2 + _vec.m_y ** 2)

    @staticmethod
    def Normalized(self) -> Vector2:
        magnitude = self.Magnitude()
        if magnitude == 0:
            return Vector2.Zero()  # 크기가 0인 경우 Zero 벡터 반환
        return Vector2(self.__x / magnitude, self.__y / magnitude)

    @staticmethod
    def Floor(_value: float, _interval: float = 1.0, _offset=0) -> float:
        return floor((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Flip(_value: Vector2, _over: Vector2 = None) -> Vector2:
        if _over is None:
            _over = Vector2(0.0, 0.0)

        return -(_value - _over) + _over

    @staticmethod
    def Angle(_vec: Vector2) -> float:
        return atan2(_vec.m_y, _vec.m_x)

    @staticmethod
    def Lerp(_lhs: Vector2, _rhs: Vector2, amount: float) -> Vector2:
        return _lhs + (_rhs - _lhs) * amount

    @staticmethod
    def Dot(_lhs: Vector2, _rhs: Vector2) -> float:
        return dot([_lhs.m_x, _lhs.m_y], [_rhs.m_x, _rhs.m_y])

    @staticmethod
    def MidPoint(_lhs: Vector2, _rhs: Vector2) -> Vector2:
        return (_lhs + _rhs) / 2.0

    @staticmethod
    def AngleToVector2(_angle: float) -> 'Vector2':
        return Vector2(cos(_angle), sin(_angle))

    @staticmethod
    def Highest(self, _lhs: 'Vector2', _rhs: 'Vector2', direction: float) -> float:
        if MathF.Equalf(direction, 0.0): return _lhs.m_x - _rhs.m_x
        if MathF.Equalf(direction, MathF.halfPi): return _lhs.m_y - _rhs.m_y
        if MathF.Equalf(direction, MathF.pi): return _rhs.m_x - _lhs.m_x
        if MathF.Equalf(direction, MathF.oneThreeFourthsPi): return _rhs.m_y - _lhs.m_y

        diff: Vector2 = self.Project(_lhs, direction) - self.Project(_rhs, direction)
        return diff.Magnitude if (abs(MathF.Angle(diff) - direction) < MathF.halfPi) else -(diff.Magnitude)

    @staticmethod
    def Highest(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.Highest(_lhs, _rhs, MathF.halfPi)

    @dispatch(Vector2, float)
    @staticmethod
    def Project(self, _vec, _angle) -> Vector2:
        return self.HighestVVF(_vec, Vector2(), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(self, _lhs, _rhs, _angle) -> Vector2:
        return self.Proportion(_lhs, _rhs, _rhs + (Vector2(cos(_angle), sin(_angle))))

    @staticmethod
    def IsPerp(_lhs: Vector2, _rhs: Vector2) -> bool:
        return MathF.Equalf(0.0, MathF.Dot(_lhs, _rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def Project(_vec: 'Vector2', _angle: float) -> 'Vector2':
        return MathF.Project2(_vec, Vector2(0.0, 0.0), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(_lhs: 'Vector2', _rhs: Vector2, _angle: float) -> 'Vector2':
        return MathF.Project(_lhs, _rhs, _rhs + Vector2(cos(_angle), sin(_angle)))

    @dispatch(Vector2, Vector2, Vector2)
    @staticmethod
    def Project(_vec: Vector2, _lineA: Vector2, _lineB: Vector2) -> 'Vector2':
        ab: Vector2 = _lineB - _lineA
        return _lineA + _vec.dot(_vec - _lineA, ab) / MathF.Dot(ab, ab) * ab

    @dispatch(Vector2, Vector2)
    @staticmethod
    def ScalarProjection(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ScalarProjection2(_lhs, MathF.Angle(_lhs) - MathF.Angle(_rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def ScalarProjection(self, _vec: Vector2, _theta: float) -> float:
        return self.megitude * cos(_theta)

    @staticmethod
    def ScalarProjectionAbs(_vec: Vector2, _theta: float) -> float:
        return MathF.Magnitude(_vec) * cos(MathF.Angle(_vec) - _theta)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy2(_point, _angle, Vector2(0.0, 0.0))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        s: float = sin(_angle)
        c: float = cos(_angle)

        nPoint: Vector2 = _point - _origin

        return Vector2(nPoint.m_x * c - nPoint.m_y * s + _origin.m_x, nPoint.m_x * s + nPoint.m_y * c + _origin.m_y)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateTo(_point: Vector2, _angle: float) -> Vector2:
        return MathF.RotateBy(_point, _angle - MathF.Angle(_point))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateTo(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        return MathF.RotateBy(_point, _angle - atan2(_point.m_y - _origin.m_y, _point.m_x - _origin.m_x), _origin)

    @staticmethod
    def ShortesArc(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc(MathF.Angle(_lhs), MathF.Angle(_rhs))

    @staticmethod
    def ShortesArcToDegree(_lhs: Vector2, _rhs: Vector2) -> float:
        return MathF.ShortesArc_ByFloat(MathF.Angle(_lhs) * rad2deg(1), MathF.Angle(_rhs) * rad2deg(1))
