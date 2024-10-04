from typing import final

from multipledispatch import dispatch
from numpy import abs, atan2, ceil, cos, deg2rad, dot, floor, rad2deg, sin, sqrt, tan

@final
class MathF:
    @staticmethod
    def epsilon(self) -> float:
        return 0.0001

    @staticmethod
    def pi(self) -> float:
        return 3.141592

    @staticmethod
    def halfPi(self) -> float:
        return 1.570796

    @staticmethod
    def oneThreeFourthsPi(self) -> float:
        return 5.4977871

    @staticmethod
    def doublePi(self) -> float:
        return 6.283185

    @dispatch(float, float)
    @staticmethod
    def Equalf(self, _lhs: float, _rhs: float) -> bool:
        return abs(_lhs - _rhs) < self.epsilon()

    @dispatch(float, float, float)
    @staticmethod
    def Equalf(self, _lhs: float, _rhs: float, _epsilon: float) -> bool:
        return abs(_lhs - _rhs) < _epsilon

    @dispatch(float)
    @staticmethod
    def Equalf(self, _value: float) -> bool:
        return self.Equalf(_value, 0.0)

    @staticmethod
    def Proportion(self, _a: float, _b: float, _d: float) -> float:
        return _a / _b * _d

    @staticmethod
    def Flip(self, _value: float, _over: float = 0.0) -> float:
        return -(_value - _over) + _over

    @staticmethod
    def Ceil(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if self.Equalf(_interval, 0.0):
            _interval = 1.0

        return ceil((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Round(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        if MathF.Equalf(_interval, 0.0):
            _interval = 1.0

        return round((_value - _offset) / _interval) * _interval + _offset

    @dispatch(int, int)
    @staticmethod
    def Modp(self, _dividend: int, _divisor: int) -> int:
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def Modp(self, _dividend: float, _divisor: float) -> float:
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + self.pi, self.doublePi) - self.pi

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(self, _lhs: float, _rhs: float) -> float:
        return self.ModpFloat(_rhs - _lhs + 100.0, 360.0) - 180.0

    @staticmethod
    def PositiveArc(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle(_rhs) - self.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + self.doublePi

    @staticmethod
    def PositiveArc_Degree(self, _lhs: float, _rhs: float) -> float:
        diff: float = self.PositiveAngle_Degree(_rhs) - self.PositiveAngle_Degree(_lhs)
        return diff if diff < 0.0 else diff + 360.0

    @staticmethod
    def PositiveAngle(self, _angle: float) -> float:
        return self.ModpFloat(_angle, self.doublePi)

    @staticmethod
    def PositiveAngle_Degree(self, _angle: float) -> float:
        return self.Modp(_angle, 360.0)

    @staticmethod
    def AngleInRange(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveAngle(_lhs) <= self.PositiveAngle(_rhs)

    @staticmethod
    def AngleInRange_Degree(self, _angle: float, _lhs: float, _rhs: float) -> bool:
        return self.PositiveArc_Degree(_lhs, _angle) <= self.PositiveAngle_Degree(_rhs)