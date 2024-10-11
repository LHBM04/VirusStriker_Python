from __future__ import annotations
from abc import abstractmethod

from Core.Objects.Object import Object

class GameObject(Object):
    """
    게임 내 렌더링되는 모든 객체입니다.
    """
    def __init__(self):
        super().__init__()
        self.__isActiveSelf: bool = True

    # region Properties
    @property
    def gameObject(self) -> GameObject:
        """
        해당 Game Object 자신을 반환합니다.
        :return: 해당 Game Object 자기 자신.
        """
        return self

    @property
    def name(self) -> str:
        """
        해당 Game Object의 이름을 반환합니다.
        :return: 해당 Game Object의 이름.
        """
        return self.__name

    @name.setter
    def name(self, _name) -> None:
        """
        해당 Game Object의 이름을 설정합니다.
        :param _name: 해당 Game Object의 새로운 이름.
        """
        self.__name = _name
    @property
    def isActiveSelf(self) -> bool:
        """
        해당 Game Object가 활성화 되어 있는지에 대한 여부를 반환합니다.
        :return: 해당 Game Object의 활성화 여부.
        """
        return self.__isActiveSelf

    @property
    def isActive(self) -> bool:
        """
        부모 Game Object를 비롯하여, 자기 자신이 활성화 되어 있는지에 대한 여부를 반환합니다.
        :return: 부모 Game Object를 비롯하여, 자기 자신이 활성화 되어 있는지에 대한 여부.
        """
        return self.__isActiveSelf
    # endregion
    # region Life-Cycle
    def Start(self) -> None:
        """
        해당 Game Object가 탄생했을 때 한번 실행됩니다.
        (※ 해당 Game Object를 관리하는 Controller/Manager에 추가된 시점을 의미합니다.)
        """
        super().Start()

    @abstractmethod
    def Update(self) -> None:
        """
        해당 Game Object의 상태를 매 프레임 갱신합니다.
        (※ 게임 루프 내에서 매 프레임 호출됩니다.)
        """
        pass

    @abstractmethod
    def FixedUpdate(self) -> None:
        """
        해당 Game Object의 물리 연산과 같은 고정된 주기의 업데이트를 처리합니다.
        (※ 물리 연산이나 시간에 의존적인 처리는 이 메서드에서 처리됩니다.)
        """
        pass

    def OnDestroy(self) -> None:
        """
        해당 Game Object가 파괴될 때 한번 실행됩니다.
        (※ 해당 Game Object를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        super().OnDestroy()
    # endregion
