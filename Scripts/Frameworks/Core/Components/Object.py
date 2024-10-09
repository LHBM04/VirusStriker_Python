from abc import ABCMeta

class Object(metaclass = ABCMeta):
    def __init__(self):
        self.__name: str        = "New Object"  # 해당 오브젝트의 이름.
        self.__isDestroy: bool  = False         # 해당 오브젝트의 파괴 여부.

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

    @isDestroy.setter
    def isDestroy(self, _destroy) -> None:
        if _destroy:
            Object.Destroy(self)

    #endregion
    def OnDestroy(self):
        pass

    @staticmethod
    def Destroy(_object: 'Object') -> None:
        _object.__isDestroy = False
