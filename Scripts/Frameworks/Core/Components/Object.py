from abc import ABCMeta
from typing import final

g_instanceID: int = 0

class Object(metaclass = ABCMeta):
    def __init__(self):
        global g_instanceID

        self.__instanceID: int  = (g_instanceID := g_instanceID + 1) - 1    # Object마다 붙는 고유의 일련 번호.
        self.__name: str        = ""                                        # 해당 Object의 이름.
        self.__isDestroy: bool  = False                                     # 해당 Object의 파괴 여부.

    # [Operator Override]
    def __eq__(self, _other: 'Object') -> bool:
        return self.__instanceID is _other.__instanceID

    def __ne__(self, _other: 'Object') -> bool:
        return not self.__eq__(_other)

    #region [Properties]
    # 해당 오브젝트의 ID를 가져옵니다. (Read-Only)
    @final
    @property
    def instanceID(self) -> int:
        return self.__instanceID

    # 해당 오브젝트의 이름을 가져옵니다.
    @property
    def name(self) -> str:
        return self.__name

    # 해당 오브젝트의 이름을 설정합니다.
    @name.setter
    def name(self, _name) -> None:
        self.__name = _name

    # 해당 Object의 파괴 여부를 가져옵니다.
    @property
    def isDestroy(self) -> bool:
        return self.__isDestroy

    # 해당 Object의 파괴 여부를 설정합니다.
    @isDestroy.setter
    def isDestroy(self, _destroy: bool):
        self.__isDestroy = _destroy
    #endregion
    #region [Life-Cycle]
    # 해당 Object가 파괴되었을 때 한번만 실행됩니다.
    def OnDestroy(self):
        pass
    #endregion