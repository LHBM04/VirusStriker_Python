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

        from Core.Behaviors.Behavior import BehaviorController
        from Core.Components.Component import ComponentController

        self.__componentController: ComponentController = ComponentController(self)
        self.__behaviorController: BehaviorController   = BehaviorController(self)

        from Core.Components.Transform import Transform

        self.__transform: Transform = self.__componentController.AddComponent(Transform)

    # region Properties
    @property
    def gameObject(self) -> GameObject:
        """
        해당 Game Object 자신을 반환합니다.
        :return: 해당 Game Object 자기 자신.
        """
        return self

    @property
    def transform(self) -> 'Transform':
        return self.__transform

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
    @abstractmethod
    def Start(self) -> None:
        """
        해당 Game Object가 탄생했을 때 한번 실행됩니다.
        (※ 해당 Game Object를 관리하는 Controller/Manager에 추가된 시점을 의미합니다.)
        """
        super().Start()

    @abstractmethod
    def Update(self, _deltaTime: float) -> None:
        """
        해당 Game Object의 상태를 매 프레임 갱신합니다.
        (※ 게임 루프 내에서 매 프레임 호출됩니다.)
        :param _deltaTime: 이전 프레임과 현재 프레임 사이의 시간 간격(초 단위).
        """
        self.__behaviorController.Update(_deltaTime)

    @abstractmethod
    def FixedUpdate(self, _fixedDeltaTime: float) -> None:
        """
        해당 Game Object의 물리 연산과 같은 고정된 주기의 업데이트를 처리합니다.\n
        (※ 물리 연산이나 시간에 의존적인 처리는 이 메서드에서 처리됩니다.)
        :param _fixedDeltaTime: 고정 업데이트 주기 동안의 시간 간격(초 단위).
        """
        self.__componentController.FixedUpdate()
        self.__behaviorController.FixedUpdate(_fixedDeltaTime)

    @abstractmethod
    def OnDestroy(self) -> None:
        """
        해당 Game Object가 파괴될 때 한번 실행됩니다.\n
        (※ 해당 Game Object를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        super().OnDestroy()

        map(lambda component: Object.Destroy(component), self.__componentController)    # 컴포넌트 파괴
        map(lambda behavior: Object.Destroy(behavior), self.__behaviorController)       # 행동 파괴
        map(lambda child: Object.Destroy(child), self.transform.children)               # 자식 파괴
    # endregion
