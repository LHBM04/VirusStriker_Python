from abc import ABCMeta

GLOBAL_INSTANCE_ID = 0
def SetGlobalInstanceID() -> int:
    global  GLOBAL_INSTANCE_ID
    GLOBAL_INSTANCE_ID += 1
    return GLOBAL_INSTANCE_ID

# 게임 내 생성될 모든 오브젝트의 베이스.
class Object(metaclass = ABCMeta):
    def __init__(self):
        self.__name: str = ""
        self.__instanceID: int = SetGlobalInstanceID()

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, _newName: str) -> None:
        self.__name = _newName

    @property
    def instanceID(self) -> int:
        return self.__instanceID

    def __eq__(self, other) -> bool:
        pass