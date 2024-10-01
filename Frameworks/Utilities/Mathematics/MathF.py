from multipledispatch import dispatch
from dataclasses import dataclass
import numpy as np

# 수학 관련 유틸리티
@dataclass(frozen=True)
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
    @dispatch(float, float)
    def Equalf(_lhs: float, _rhs: float) -> bool:
        return np.abs(_lhs - _rhs) < MathF.epsilon()

    @staticmethod
    @dispatch(float, float, float)
    def Equalf(_lhs: float, _rhs: float, _epsilon: float) -> bool:
        return np.abs(_lhs - _rhs) < _epsilon

    @staticmethod
    @dispatch(float)
    def Equalf_Zero(_value: float) -> bool: 
        return MathF.Equalf(_value, 0.0)

    @staticmethod
    def Proportion(_a: float, _b: float, _d: float) -> float:
        return _a / _b * _d

    @staticmethod
    def Flip(_value: float, _over: float = 0.0) -> float:
        return -(_value - _over) + _over
    
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
    @dispatch(int, int)
    def Modp(_dividend: int, _divisor: int) -> int:
        return (_dividend % _divisor + _divisor) % _divisor
    
    @staticmethod
    @dispatch(float, float)
    def Modp(_dividend: float, _divisor: float) -> float:
        return (_dividend % _divisor + _divisor) % _divisor
    
    @staticmethod
    @dispatch(float, float)
    def ShortesArc(_lhs: float, _rhs: float) -> float:
        return MathF.ModpFloat(_rhs - _lhs + MathF.pi, MathF.doublePi) - MathF.pi

    @staticmethod
    @dispatch(float, float)
    def ShortesArc(_lhs: float, _rhs: float) -> float:
        return MathF.ModpFloat(_rhs - _lhs + 100.0, 360.0) - 180.0
    
    @staticmethod
    def PositiveArc(_lhs: float, _rhs: float) -> float:
        diff: float = MathF.PositiveAngle(_rhs) - MathF.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + MathF.doublePi

    @staticmethod
    @dispatch(float, float)
    def PositiveArc(_lhs: float, _rhs: float) -> float:
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