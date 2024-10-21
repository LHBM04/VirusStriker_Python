from __future__ import annotations
from typing import final

from multipledispatch import dispatch
from numpy import *

@final
class MathF:
    """
    실수 계산 관련 상수와 유틸리티 메서드를 제공합니다.
    """
    @staticmethod
    def epsilon() -> float:
        """
        부동소수점 비교에 사용할 작은 값(엡실론)을 반환합니다.
        :return: 엡실론 값 (0.0001)
        """
        return 0.0001

    @staticmethod
    def pi() -> float:
        """
        파이(π) 값을 반환합니다.
        :return: 파이 값 (3.141592)
        """
        return 3.141592

    @staticmethod
    def halfPi() -> float:
        """
        파이의 절반 값을 반환합니다.
        :return: 반 파이 값 (1.570796)
        """
        return 1.570796

    @staticmethod
    def oneThreeFourthsPi() -> float:
        """
        3/2 파이 값을 반환합니다.
        :return: 3/2 파이 값 (5.4977871)
        """
        return 5.4977871

    @staticmethod
    def doublePi() -> float:
        """
        두 배의 파이 값을 반환합니다.
        :return: 2π 값 (6.283185)
        """
        return 6.283185

    @dispatch(float, float)
    @staticmethod
    def Equalf(_lhs: float, _rhs: float) -> bool:
        """
        두 부동소수점 수를 비교하여, 차이가 엡실론 값보다 작은지 확인합니다.
        :param _lhs: 비교할 첫 번째 값
        :param _rhs: 비교할 두 번째 값
        :return: 두 값이 거의 동일하면 True, 그렇지 않으면 False
        """
        return abs(_lhs - _rhs) < MathF.epsilon()

    @dispatch(float, float, float)
    @staticmethod
    def Equalf(_lhs: float, _rhs: float, _epsilon: float) -> bool:
        """
        두 부동소수점 수를 주어진 엡실론 값으로 비교합니다.
        :param _lhs: 비교할 첫 번째 값
        :param _rhs: 비교할 두 번째 값
        :param _epsilon: 비교에 사용할 엡실론 값
        :return: 두 값이 주어진 엡실론 내에서 동일하면 True
        """
        return abs(_lhs - _rhs) < _epsilon

    @dispatch(float)
    @staticmethod
    def Equalf(_value: float) -> bool:
        """
        입력된 부동소수점 수가 0과 동일한지 확인합니다.
        :param _value: 비교할 값
        :return: 값이 0과 거의 동일하면 True
        """
        return MathF.Equalf(_value, 0.0)

    @staticmethod
    def Proportion(self, _a: float, _b: float, _d: float) -> float:
        """
        주어진 두 값의 비율을 계산합니다.
        :param _a: 첫 번째 값
        :param _b: 두 번째 값
        :param _d: 비율을 적용할 값
        :return: 비율을 적용한 값
        """
        return _a / _b * _d

    @staticmethod
    def Flip(self, _value: float, _over: float = 0.0) -> float:
        """
        주어진 값을 기준 값(_over)을 중심으로 뒤집습니다.
        :param _value: 뒤집을 값
        :param _over: 기준 값 (기본값은 0.0)
        :return: 뒤집어진 값
        """
        return -(_value - _over) + _over

    @staticmethod
    def Ceil(self, _value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        """
        주어진 값을 특정 간격(interval)으로 올림한 결과를 반환합니다.
        :param _value: 올림할 값
        :param _interval: 간격 (기본값은 1.0)
        :param _offset: 오프셋 값 (기본값은 0.0)
        :return: 올림된 값
        """
        if self.Equalf(_interval, 0.0):
            _interval = 1.0
        return ceil((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Round(_value: float, _interval: float = 1.0, _offset: float = 0.0) -> float:
        """
        주어진 값을 특정 간격(interval)으로 반올림한 결과를 반환합니다.
        :param _value: 반올림할 값
        :param _interval: 간격 (기본값은 1.0)
        :param _offset: 오프셋 값 (기본값은 0.0)
        :return: 반올림된 값
        """
        if MathF.Equalf(_interval, 0.0):
            _interval = 1.0
        return round((_value - _offset) / _interval) * _interval + _offset

    @dispatch(int, int)
    @staticmethod
    def Modp(_dividend: int, _divisor: int) -> int:
        """
        두 정수의 모듈로 연산 결과를 반환합니다. 결과는 양수입니다.
        :param _dividend: 피제수 (나누어지는 수)
        :param _divisor: 제수 (나누는 수)
        :return: 양수 모듈로 연산 결과
        """
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def Modp(_dividend: float, _divisor: float) -> float:
        """
        두 실수의 모듈로 연산 결과를 반환합니다. 결과는 양수입니다.
        :param _dividend: 피제수 (나누어지는 수)
        :param _divisor: 제수 (나누는 수)
        :return: 양수 모듈로 연산 결과
        """
        return (_dividend % _divisor + _divisor) % _divisor

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(_lhs: float, _rhs: float) -> float:
        """
        두 각도 간의 최단 호(arc)를 계산하여 반환합니다.
        :param _lhs: 첫 번째 각도
        :param _rhs: 두 번째 각도
        :return: 최단 호 값
        """
        return MathF.Modp(_rhs - _lhs + MathF.pi(), MathF.doublePi()) - MathF.pi()

    @dispatch(float, float)
    @staticmethod
    def ShortesArc(_lhs: float, _rhs: float) -> float:
        """
        주어진 각도 범위에서 최단 호(arc)를 계산하여 반환합니다.
        :param _lhs: 첫 번째 각도
        :param _rhs: 두 번째 각도
        :return: 최단 호 값
        """
        return MathF.Modp(_rhs - _lhs + 100.0, 360.0) - 180.0

    @staticmethod
    def PositiveArc(_lhs: float, _rhs: float) -> float:
        """
        두 각도 사이의 양의 호(arc)를 계산하여 반환합니다.
        :param _lhs: 첫 번째 각도
        :param _rhs: 두 번째 각도
        :return: 양의 호 값
        """
        diff: float = MathF.PositiveAngle(_rhs) - MathF.PositiveAngle(_lhs)
        return diff if diff < 0.0 else diff + MathF.doublePi()

    @staticmethod
    def PositiveArc_Degree(_lhs: float, _rhs: float) -> float:
        """
        주어진 각도 사이의 양의 호(arc)를 계산하여 반환합니다. 각도는 도(degree) 단위입니다.
        :param _lhs: 첫 번째 각도
        :param _rhs: 두 번째 각도
        :return: 양의 호 값 (도 단위)
        """
        diff: float = MathF.PositiveAngle_Degree(_rhs) - MathF.PositiveAngle_Degree(_lhs)
        return diff if diff < 0.0 else diff + 360.0

    @staticmethod
    def PositiveAngle(_angle: float) -> float:
        """
        주어진 각도를 양의 각도로 변환합니다.
        :param _angle: 변환할 각도
        :return: 양의 각도로 변환된 값
        """
        return MathF.Modp(_angle, MathF.doublePi())

    @staticmethod
    def PositiveAngle_Degree(_angle: float) -> float:
        """
        주어진 각도를 0도에서 360도 사이의 양의 각도로 변환합니다.
        :param _angle: 변환할 각도
        :return: 양의 각도로 변환된 값 (도 단위)
        """
        return MathF.Modp(_angle, 360.0)

    @staticmethod
    def AngleInRange(_angle: float, _lhs: float, _rhs: float) -> bool:
        """
        주어진 각도가 특정 범위 내에 있는지 확인합니다.
        :param _angle: 확인할 각도
        :param _lhs: 범위의 시작 각도
        :param _rhs: 범위의 끝 각도
        :return: 각도가 범위 내에 있으면 True
        """
        return MathF.PositiveAngle(_lhs) <= MathF.PositiveAngle(_rhs)

    @staticmethod
    def AngleInRange_Degree(_angle: float, _lhs: float, _rhs: float) -> bool:
        """
        주어진 각도가 특정 범위 내에 있는지 확인합니다. 각도는 도(degree) 단위입니다.
        :param _angle: 확인할 각도
        :param _lhs: 범위의 시작 각도
        :param _rhs: 범위의 끝 각도
        :return: 각도가 범위 내에 있으면 True
        """
        return MathF.PositiveArc_Degree(_lhs, _angle) <= MathF.PositiveAngle_Degree(_rhs)

@final
class Vector2:
    """
    2D 벡터를 나타내는 클래스.
    """
    def __init__(self, _x: float = 0.0, _y: float = 0.0) -> None:
        """
        Vector2 객체를 초기화합니다.
        :param _x: x 좌표, 기본값은 0.0입니다.
        :param _y: y 좌표, 기본값은 0.0입니다.
        """
        self.__x: float = _x
        self.__y: float = _y

    # [Operation Override] #
    def __neg__(self) -> Vector2:
        """
        벡터의 반대 방향 벡터를 반환합니다.
        :return: 현재 벡터의 반대 방향을 나타내는 Vector2 객체.
        """
        return Vector2(-self.__x, -self.__y)

    def __add__(self, _other: Vector2) -> Vector2:
        """
        두 벡터를 더합니다.
        :param _other: 더할 다른 Vector2 객체.
        :return: 두 벡터의 합을 나타내는 Vector2 객체.
        """
        return Vector2(self.__x + _other.__x, self.__y + _other.__y)

    def __sub__(self, _other: Vector2) -> Vector2:
        """
        두 벡터를 뺍니다.
        :param _other: 뺄 다른 Vector2 객체.
        :return: 두 벡터의 차를 나타내는 Vector2 객체.
        """
        return Vector2(self.__x - _other.__x, self.__y - _other.__y)

    def __mul__(self, _other: float) -> Vector2:
        """
        벡터를 스칼라 값으로 곱합니다.
        :param _other: 곱할 스칼라 값.
        :return: 곱셈 결과를 나타내는 Vector2 객체.
        """
        return Vector2(self.__x * _other, self.__y * _other)

    def __truediv__(self, _other: float) -> Vector2:
        """
        벡터를 스칼라 값으로 나눕니다.
        :param _other: 나눌 스칼라 값.
        :return: 나눗셈 결과를 나타내는 Vector2 객체.
        """
        return Vector2(self.__x / _other, self.__y / _other)

    def __eq__(self, _other: Vector2) -> bool:
        """
        두 벡터가 같은지 비교합니다.
        :param _other: 비교할 다른 Vector2 객체.
        :return: 두 벡터가 같으면 True, 아니면 False.
        """
        return MathF.Equalf(float(self.__x), _other.__x) and MathF.Equalf(float(self.__y), _other.__y)

    def __ne__(self, _other: Vector2) -> bool:
        """
        두 벡터가 다른지 비교합니다.
        :param _other: 비교할 다른 Vector2 객체.
        :return: 두 벡터가 다르면 True, 같으면 False.
        """
        return not self.__eq__(_other)

    # [Properties] #
    @property
    def x(self) -> float:
        """
        x 좌표를 가져옵니다.
        :return: x 좌표의 값.
        """
        return self.__x

    @x.setter
    def x(self, _x: float) -> None:
        """
        x 좌표를 설정합니다.
        :param _x: 설정할 x 좌표의 값.
        """
        self.__x = _x

    @property
    def y(self) -> float:
        """
        y 좌표를 가져옵니다.
        :return: y 좌표의 값.
        """
        return self.__y

    @y.setter
    def y(self, _y: float) -> None:
        """
        y 좌표를 설정합니다.
        :param _y: 설정할 y 좌표의 값.
        """
        self.__y = _y

    @staticmethod
    def Zero() -> Vector2:
        """
        원점(0, 0)을 나타내는 벡터를 반환합니다.
        :return: (0.0, 0.0)을 나타내는 Vector2 객체.
        """
        return Vector2(0.0, 0.0)

    @staticmethod
    def Up() -> Vector2:
        """
        위 방향을 나타내는 벡터를 반환합니다.
        :return: (0.0, 1.0)을 나타내는 Vector2 객체.
        """
        return Vector2(0.0, 1.0)

    @staticmethod
    def Down() -> Vector2:
        """
        아래 방향을 나타내는 벡터를 반환합니다.
        :return: (0.0, -1.0)을 나타내는 Vector2 객체.
        """
        return Vector2(0.0, -1.0)

    @staticmethod
    def Left() -> Vector2:
        """
        왼쪽 방향을 나타내는 벡터를 반환합니다.
        :return: (-1.0, 0.0)을 나타내는 Vector2 객체.
        """
        return Vector2(-1.0, 0.0)

    @staticmethod
    def Right() -> Vector2:
        """
        오른쪽 방향을 나타내는 벡터를 반환합니다.
        :return: (1.0, 0.0)을 나타내는 Vector2 객체.
        """
        return Vector2(1.0, 0.0)

@final
class MathVec:
    """
    벡터에 대한 다양한 수학적 연산 관련 유틸리티 메서드를 제공합니다.
    """
    @staticmethod
    def Magnitude(_vec: Vector2) -> float:
        """
        주어진 벡터의 크기를 계산합니다.
        :param _vec: 크기를 계산할 Vector2 객체.
        :return: 벡터의 크기.
        """
        return sqrt(_vec.x ** 2 + _vec.y ** 2)

    @staticmethod
    def Normalized(_vec: Vector2) -> Vector2:
        """
        벡터를 정규화합니다. (크기를 1로 만듭니다)
        :return: 정규화된 Vector2 객체.
        """
        magnitude = MathVec.Magnitude(_vec)
        if magnitude == 0:
            return Vector2.Zero()  # 크기가 0인 경우 Zero 벡터 반환

        return Vector2(_vec.x / magnitude, _vec.y / magnitude)

    @staticmethod
    def Floor(_value: float, _interval: float = 1.0, _offset=0) -> float:
        """
        주어진 값을 특정 간격으로 내림합니다.
        :param _value: 내림할 값.
        :param _interval: 내림 간격, 기본값은 1.0입니다.
        :param _offset: 오프셋, 기본값은 0입니다.
        :return: 내림 처리된 값.
        """
        return floor((_value - _offset) / _interval) * _interval + _offset

    @staticmethod
    def Flip(_value: Vector2, _over: Vector2 = None) -> Vector2:
        """
        주어진 벡터를 특정 기준 벡터에 대해 뒤집습니다.
        :param _value: 뒤집을 Vector2 객체.
        :param _over: 기준 벡터, 기본값은 (0, 0)입니다.
        :return: 뒤집힌 벡터.
        """
        if _over is None:
            _over = Vector2(0.0, 0.0)

        return -(_value - _over) + _over

    @staticmethod
    def Angle(_vec: Vector2) -> float:
        """
        주어진 벡터의 각도를 반환합니다.
        :param _vec: 각도를 구할 Vector2 객체.
        :return: 벡터의 각도.
        """
        return atan2(_vec.y, _vec.x)

    @staticmethod
    def Lerp(_lhs: Vector2, _rhs: Vector2, amount: float) -> Vector2:
        """
        두 벡터 간의 선형 보간을 수행합니다.
        :param _lhs: 시작 벡터.
        :param _rhs: 끝 벡터.
        :param amount: 보간 비율 (0.0~1.0).
        :return: 보간된 Vector2 객체.
        """
        return _lhs + (_rhs - _lhs) * amount

    @staticmethod
    def Dot(_lhs: Vector2, _rhs: Vector2) -> float:
        """
        두 벡터의 내적을 계산합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 내적 결과.
        """
        return dot([_lhs.x, _lhs.y], [_rhs.x, _rhs.y])

    @staticmethod
    def MidPoint(_lhs: Vector2, _rhs: Vector2) -> Vector2:
        """
        두 벡터의 중점을 계산합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 중점을 나타내는 Vector2 객체.
        """
        return (_lhs + _rhs) / 2.0

    @staticmethod
    def AngleToVector2(_angle: float) -> Vector2:
        """
        각도를 주어진 방향의 벡터로 변환합니다.
        :param _angle: 변환할 각도.
        :return: 변환된 Vector2 객체.
        """
        return Vector2(cos(_angle), sin(_angle))

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Highest(self, _lhs: Vector2, _rhs: Vector2, _direction: float) -> float:
        """
        두 벡터의 방향에 따라 높은 값을 반환합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :param _direction: 비교할 방향의 각도.
        :return: 두 벡터 중 높은 값.
        """
        if MathF.Equalf(_direction, 0.0): return _lhs.x - _rhs.x
        if MathF.Equalf(_direction, MathF.halfPi()): return _lhs.y - _rhs.y
        if MathF.Equalf(_direction, MathF.pi()): return _rhs.x - _lhs.x
        if MathF.Equalf(_direction, MathF.oneThreeFourthsPi()): return _rhs.y - _lhs.y

        diff: Vector2 = self.Project(_lhs, _direction) - self.Project(_rhs, _direction)
        return self.Magnitude(diff) if (abs(MathVec.Angle(diff) - _direction) < MathF.halfPi()) else -MathVec.Magnitude(diff)

    @dispatch(Vector2, Vector2)
    @staticmethod
    def Highest(_lhs: Vector2, _rhs: Vector2) -> float:
        """
        두 벡터의 높이를 비교하여 높은 값을 반환합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 높은 값을 나타내는 float.
        """
        return MathVec.Highest(_lhs, _rhs, MathF.halfPi)

    @dispatch(Vector2, float)
    @staticmethod
    def Project(_vec: Vector2, _angle: float) -> Vector2:
        """
        주어진 벡터를 특정 각도로 투영합니다.
        :param _vec: 투영할 Vector2 객체.
        :param _angle: 투영할 각도.
        :return: 투영된 Vector2 객체.
        """
        return MathVec.Highest(_vec, Vector2(), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(_lhs: Vector2, _rhs: Vector2, _angle: float) -> Vector2:
        """
        두 벡터를 특정 각도로 투영합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :param _angle: 투영할 각도.
        :return: 투영된 Vector2 객체.
        """
        return MathF.Proportion(_lhs, _rhs, _rhs + (Vector2(cos(_angle), sin(_angle))))

    @staticmethod
    def IsPerp(_lhs: Vector2, _rhs: Vector2) -> bool:
        """
        두 벡터가 수직인지 확인합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 수직이면 True, 아니면 False.
        """
        return MathF.Equalf(0.0, MathVec.Dot(_lhs, _rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def Project(self, _vec: Vector2, _angle: float) -> Vector2:
        """
        주어진 벡터를 특정 각도로 투영합니다.
        :param _vec: 투영할 Vector2 객체.
        :param _angle: 투영할 각도.
        :return: 투영된 Vector2 객체.
        """
        return self.Project2(_vec, Vector2(0.0, 0.0), _angle)

    @dispatch(Vector2, Vector2, float)
    @staticmethod
    def Project(self, _lhs: Vector2, _rhs: Vector2, _angle: float) -> Vector2:
        """
        두 벡터를 특정 각도로 투영합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :param _angle: 투영할 각도.
        :return: 투영된 Vector2 객체.
        """
        return self.Project(_lhs, _rhs, _rhs + Vector2(cos(_angle), sin(_angle)))

    @dispatch(Vector2, Vector2, Vector2)
    @staticmethod
    def Project(self, _vec: Vector2, _lineA: Vector2, _lineB: Vector2) -> 'Vector2':
        """
        주어진 벡터를 두 선분에 투영합니다.
        :param _vec: 투영할 Vector2 객체.
        :param _lineA: 선분의 한쪽 끝.
        :param _lineB: 선분의 다른 쪽 끝.
        :return: 투영된 Vector2 객체.
        """
        ab: Vector2 = _lineB - _lineA
        return _lineA + self.Dot(_vec - _lineA, ab) / self.Dot(ab, ab) * ab

    @dispatch(Vector2, Vector2)
    @staticmethod
    def ScalarProjection(self, _lhs: Vector2, _rhs: Vector2) -> float:
        """
        두 벡터 간의 스칼라 투영을 계산합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 스칼라 투영 값.
        """
        return self.ScalarProjection(_lhs, self.Angle(_lhs) - self.Angle(_rhs))

    @dispatch(Vector2, float)
    @staticmethod
    def ScalarProjection(self, _vec: Vector2, _theta: float) -> float:
        """
        주어진 벡터의 스칼라 투영을 계산합니다.
        :param _vec: 스칼라 투영할 Vector2 객체.
        :param _theta: 각도.
        :return: 스칼라 투영 값.
        """
        return self.megitude * cos(_theta)

    @staticmethod
    def ScalarProjectionAbs(self, _vec: Vector2, _theta: float) -> float:
        """
        주어진 벡터의 절대 스칼라 투영을 계산합니다.
        :param _vec: 절대 스칼라 투영할 Vector2 객체.
        :param _theta: 각도.
        :return: 절대 스칼라 투영 값.
        """
        return self.Magnitude(_vec) * cos(self.Angle(_vec) - _theta)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateBy(self, _point: Vector2, _angle: float) -> Vector2:
        """
        주어진 포인트를 특정 각도로 회전합니다.
        :param _point: 회전할 Vector2 객체.
        :param _angle: 회전할 각도.
        :return: 회전된 Vector2 객체.
        """
        return self.RotateBy(_point, _angle, Vector2(0.0, 0.0))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateBy(_point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        """
        주어진 포인트를 특정 각도로 회전하고 기준점을 지정합니다.
        :param _point: 회전할 Vector2 객체.
        :param _angle: 회전할 각도.
        :param _origin: 회전 기준점.
        :return: 회전된 Vector2 객체.
        """
        s: float = sin(_angle)
        c: float = cos(_angle)

        nPoint: Vector2 = _point - _origin

        return Vector2(nPoint.x * c - nPoint.y * s + _origin.x, nPoint.x * s + nPoint.y * c + _origin.y)

    @dispatch(Vector2, float)
    @staticmethod
    def RotateTo(self, _point: Vector2, _angle: float) -> Vector2:
        """
        주어진 포인트를 특정 각도로 회전합니다.
        :param _point: 회전할 Vector2 객체.
        :param _angle: 회전할 각도.
        :return: 회전된 Vector2 객체.
        """
        return self.RotateBy(_point, _angle - self.Angle(_point))

    @dispatch(Vector2, float, Vector2)
    @staticmethod
    def RotateTo(self, _point: Vector2, _angle: float, _origin: Vector2) -> Vector2:
        """
        주어진 포인트를 특정 각도로 회전하고 기준점을 지정합니다.
        :param _point: 회전할 Vector2 객체.
        :param _angle: 회전할 각도.
        :param _origin: 회전 기준점.
        :return: 회전된 Vector2 객체.
        """
        return self.RotateBy(_point, _angle - atan2(_point.y - _origin.y, _point.x - _origin.x), _origin)

    @staticmethod
    def ShortesArc(self, _lhs: Vector2, _rhs: Vector2) -> float:
        """
        두 벡터 간의 가장 짧은 호의 각도를 계산합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 두 벡터 간의 가장 짧은 호의 각도.
        """
        return MathF.ShortesArc(MathVec.Angle(_lhs), MathVec.Angle(_rhs))

    @staticmethod
    def ShortesArcToDegree(_lhs: Vector2, _rhs: Vector2) -> float:
        """
        두 벡터 간의 가장 짧은 호의 각도를 도 단위로 계산합니다.
        :param _lhs: 첫 번째 Vector2 객체.
        :param _rhs: 두 번째 Vector2 객체.
        :return: 두 벡터 간의 가장 짧은 호의 각도 (도 단위).
        """
        return MathF.ShortesArc(MathVec.Angle(_lhs) * rad2deg(1), MathVec.Angle(_rhs) * rad2deg(1))