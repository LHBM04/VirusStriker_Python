from __future__ import annotations
from abc import ABCMeta, abstractmethod

from Core.Components.Component import Component

class Behavior(Component, metaclass = ABCMeta):
    """
    Game Object의 행동, 흐름을 관리하고 제어합니다.
    """
    def __init__(self, _actor: 'GameObject'):
        super().__init__(_actor)

        self.__isEnabled: bool = True

    # region Properties
    @property
    def isEnable(self) -> bool:
        """
        해당 Behavior가 활성화되어 있는지에 대한 여부를 반환합니다.
        :return: 해당 Behavior가 활성화되어 있는지에 대한 여부.
        """
        return self.__isEnabled

    @isEnable.setter
    def isEnable(self, _enable: bool) -> None:
        """
        해당 Behavior의 활성화 여부를 설정합니다.
        :param _enable: 해당 Behavior의 활성화 여부.
        """
        if _enable and not self.__isEnabled:
            self.__isEnabled = True
            self.OnEnable()
        elif not _enable and self.__isEnabled:
            self.__isEnabled = False
            self.OnDisable()

    @property
    def isActiveAndEnabled(self) -> bool:
        """
        해당 Behavior와 이를 수행하는 Game Object의 활성화 여부를 같이 반환합니다.
        :return: 해당 Behavior와 이를 수행하는 Game Object의 활성화 여부.
        """
        return self.__isEnabled and self.gameObject.isActive
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self):
        """
        해당 Behavior가 추가되었을 때 한번 실행됩니다.\n
        (※ 해당 Behavior를 수행하는 Game Object에 추가된 시점을 의미합니다.)
        :return: 
        """
        super().Start()

    @abstractmethod
    def OnEnable(self) -> None:
        """
        해당 Behavior가 활성화되었을 때 한번 실행됩니다.
        """
        pass

    @abstractmethod
    def Update(self, _deltaTime: float):
        """
        해당 Behavior의 동작을 매 프레임 갱신합니다.\n
        (※ 게임 루프 내에서 매 프레임 호출됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float):
        """
        해당 Behavior의 물리 연산과 같은 고정된 주기의 업데이트를 처리합니다.\n
        (※ 물리 연산이나 시간에 의존적인 처리는 이 메서드에서 처리됩니다.)
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def LateUpdate(self, _deltaTime: float):
        """
        해당 Behavior의 동작을 매 프레임 갱신합니다.\n
        (※ Update() 이후 실행됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 변화량(초 단위).
        """
        pass

    @abstractmethod
    def OnDisable(self) -> None:
        """
        해당 Behavior가 비활성화되었을 때 한번 실행됩니다.
        """
        pass

    @abstractmethod
    def OnDestroy(self):
        """
        해당 Behavior가 파괴되었을 때 한번 실행됩니다.
        (※ 해당 Behavior를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        :return:
        """
        super().OnDestroy()
    # endregion
