from abc import ABCMeta

class Object(metaclass = ABCMeta):
    def __init__(self):
        self.__name: str        = "New Object"  # 해당 오브젝트의 이름.
        self.__isDestroy: bool  = True          # 해당 오브젝트의 파괴 여부.

    #region [Properties]
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, _name) -> None:
        self.__name = _name

    @property
    def isDestroy(self) -> bool:
        return self.__isDestroy
    #endregion
    #region [Abstract Method]
    def OnAwake(self) -> None:
        pass

    def OnDestroy(self) -> None:
        pass

    @staticmethod
    def Destroy(self, _object: 'Object') -> None:
        _object.__isDestroy = False
        self.OnDestroy()
    #endregion