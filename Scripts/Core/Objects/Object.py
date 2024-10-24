from __future__ import annotations
from abc import ABCMeta

class Object(metaclass = ABCMeta):
    """
    해당 프레임워크에서 사용되는 모든 객체(Game Object, Component, Behavior...)의 베이스(근간).
    """
    def __init__(self):
        self.__isDestroy: bool  = False         # 해당 Object의 파괴 여부.

    # region Properties
    @property
    def isDestroy(self) -> bool:
        """
        해당 Object의 파괴 여부를 반환합니다.
        :return: 해당 Object의 파괴 여부.
        """
        return self.__isDestroy
    # endregion
    # region Life-Cycle
    def Start(self) -> None:
        """
        해당 Object가 탄생했을 때 한번 실행됩니다.
        (※ 해당 Object를 관리하는 Controller/Manager에 추가된 시점을 의미합니다.)
        """
        ...

    def OnDestroy(self) -> None:
        """
        해당 Object가 파괴될 때 한번 실행됩니다.
        (※ 해당 Object를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        ...
    # endregion
    @staticmethod
    def Destroy(_object: Object) -> None:
        """
        Object를 파괴합니다.
        :param _object: 파괴할 Object.
        """
        _object.__isDestroy = True
        _object.OnDestroy()
        del _object