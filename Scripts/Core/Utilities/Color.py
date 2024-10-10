class Color:
    """
    색상을 정의합니다. (R, G, B, A)
    """
    # region Static Methods
    @staticmethod
    def MinValue() -> int:
        """
        색깔의 최소값을 반환합니다.
        :return: 색깔의 최소값.
        """
        return 0

    @staticmethod
    def MaxValue() -> int:
        """
        색깔의 최대값을 반환합니다.
        :return: 색깔의 최대값.
        """
        return 255
    # endregion

    def __init__(self,
                 _r: int = MaxValue(),
                 _g: int = MaxValue(),
                 _b: int = MaxValue(),
                 _a: int = MaxValue()) -> None:
        """
        Color 객체를 초기화합니다.
        :param _r: 빨강(R) 색상 값.
        :param _g: 초록(G) 색상 값.
        :param _b: 파랑(B) 색상 값.
        :param _a: 투명도(A) 색상 값.
        """
        self.__r: int = max(self.MinValue(), min(_r, self.MaxValue()))
        self.__g: int = max(self.MinValue(), min(_g, self.MaxValue()))
        self.__b: int = max(self.MinValue(), min(_b, self.MaxValue()))
        self.__a: int = max(self.MinValue(), min(_a, self.MaxValue()))

    # region Operation Override
    def __eq__(self, _other: 'Color') -> bool:
        """
        두 Color 객체가 같은지 비교합니다.
        :param _other: 비교할 다른 Color 객체.
        :return: 같은 경우 True, 그렇지 않으면 False.
        """
        return (self.r == _other.r and
                self.g == _other.g and
                self.b == _other.b and
                self.a == _other.a)

    def __ne__(self, _other: 'Color') -> bool:
        """
        두 Color 객체가 다른지 비교합니다.
        :param _other: 비교할 다른 Color 객체.
        :return: 다른 경우 True, 그렇지 않으면 False.
        """
        return not self.__eq__(_other)
    # endregion

    # region Properties
    @property
    def r(self) -> int:
        """
        빨강(R) 색상 값을 반환합니다.
        :return: 빨강 색상 값.
        """
        return self.__r

    @r.setter
    def r(self, _r: int) -> None:
        """
        빨강(R) 색상 값을 설정합니다.
        :param _r: 설정할 빨강 색상 값.
        """
        self.__r = max(self.MinValue(), min(_r, self.MaxValue()))

    @property
    def g(self) -> int:
        """
        초록(G) 색상 값을 반환합니다.
        :return: 초록 색상 값.
        """
        return self.__g

    @g.setter
    def g(self, _g: int) -> None:
        """
        초록(G) 색상 값을 설정합니다.
        :param _g: 설정할 초록 색상 값.
        """
        self.__g = max(self.MinValue(), min(_g, self.MaxValue()))

    @property
    def b(self) -> int:
        """
        파랑(B) 색상 값을 반환합니다.
        :return: 파랑 색상 값.
        """
        return self.__b

    @b.setter
    def b(self, _b: int) -> None:
        """
        파랑(B) 색상 값을 설정합니다.
        :param _b: 설정할 파랑 색상 값.
        """
        self.__b = max(self.MinValue(), min(_b, self.MaxValue()))

    @property
    def a(self) -> int:
        """
        투명도(A) 색상 값을 반환합니다.
        :return: 투명도 색상 값.
        """
        return self.__a

    @a.setter
    def a(self, _a: int) -> None:
        """
        투명도(A) 색상 값을 설정합니다.
        :param _a: 설정할 투명도 색상 값.
        """
        self.__a = max(self.MinValue(), min(_a, self.MaxValue()))
    # endregion
