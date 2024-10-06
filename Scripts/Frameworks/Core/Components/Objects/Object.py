from abc import ABCMeta, abstractmethod

GLOBAL_INSTANCE_ID = -1 # 오브젝트에 붙여지는 고유 ID.

# 오브젝트에 번호를 부여합니다.
def GetGlobalInstanceID() -> int:
    global  GLOBAL_INSTANCE_ID
    GLOBAL_INSTANCE_ID += 1
    return GLOBAL_INSTANCE_ID

# 게임 내 생성될 모든 오브젝트의 베이스.
class Object(metaclass = ABCMeta):
    def __init__(self):
        self.__name: str = "New Object"
        self.__instanceID: int = GetGlobalInstanceID()
        self.__isActive: bool = True
        self.__isDestroy: bool = False

    # 해당 오브젝트의 이름(Getter).
    @property
    def name(self) -> str:
        return self.__name

    # 해당 오브젝트의 이름(Setter).
    @name.setter
    def name(self, _newName: str) -> None:
        self.__name = _newName

    # 해당 오브젝트의 ID.
    @property
    def instanceID(self) -> int:
        return self.__instanceID

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, _active: bool) -> None:
        self.__isActive = _active

    @property
    def isDestroy(self) -> bool:
        return self.__isDestroy

    @isDestroy.setter
    def isDestroy(self, _destroy: bool) -> None:
        self.__isDestroy = _destroy

    def __eq__(self, _other: 'Object') -> bool:
        return self.__instanceID is _other.__instanceID

    def __ne__(self, _other: 'Object') -> bool:
        return not self.__eq__(_other)

    # 해당 오브젝트가 'Game Object Manager'에 추가될 때 실행됩니다.
    @abstractmethod
    def Start(self) -> None:
        pass

    # 매 프레임마다 실행됩니다.
    # ※ Object 상속 받은 클래스 작성할 때 반드시 부모 FixedUpdate() 호출할 것!
    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        pass

    # 매 고정 프레임마다 실행됩니다.
    # ※ Object 상속 받은 클래스 작성할 때 반드시 부모 FixedUpdate() 호출할 것!
    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        pass

    # Update() 이후 실행됩니다.
    @abstractmethod
    def LateUpdate(self, _deltaTime: float) -> None:
        pass

    # 해당 인스턴스가 파괴되었을 때 실행됩니다.
    @abstractmethod
    def Destroy(self):
        pass