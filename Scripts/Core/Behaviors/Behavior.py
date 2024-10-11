from abc import ABCMeta, abstractmethod

from Core.Components.Component import Component
from Core.Objects.GameObject import GameObject

class Behavior(Component, metaclass = ABCMeta):
    """
    Game Object의 행동, 흐름을 관리하고 제어합니다.
    """
    def __init__(self, _actor: GameObject):
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
    def isEnable(self, _enable) -> None:
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
        :return:  해당 Behavior와 이를 수행하는 Game Object의 활성화 여부.
        """
        return self.__isEnabled and self.gameObject.isActive
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self):
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
        매 프레임마다 실행됩니다.
        :param _deltaTime: 현재 시간 변화량.
        """
        pass

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float):
        """
        0.02초마다 고정적으로 실행됩니다.
        :param _fixedDeltaTime: 현재 시간 변화량.
        """
        pass

    @abstractmethod
    def LateUpdate(self, _deltaTime: float):
        """
        매 프레임마다 Update() 이후 실행됩니다.
        :param _deltaTime: 현재 시간 변화량.
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
        super().OnDestroy()
    # endregion