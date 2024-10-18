from abc import ABCMeta, abstractmethod

from Core.Objects.Object import Object

class Component(Object, metaclass = ABCMeta):
    """
    Game Object의 정보 및 속성을 저장 및 제어합니다.
    """
    def __init__(self, _owner: 'GameObject'):
        super().__init__()

        from Core.Objects.GameObject import GameObject
        self.__owner: GameObject = _owner # 해당 Component의 주인.

    # region Properties
    @property
    def gameObject(self) -> 'GameObject':
        """
        해당 Component의 Owner를 반환합니다.
        :return: 해당 Component의 Owner.
        """
        return self.__owner

    @property
    def name(self) -> str:
        """
        해당 Component의 Owner의 이름을 반환합니다.
        :return: 해당 Component의 Owner의 이름.
        """
        return self.__owner.name
    # endregion
    # region Life-Cycle
    @abstractmethod
    def Start(self) -> None:
        """
        해당 Component가 추가되었을 때 한번 실행됩니다.
        (※ 해당 Component를 사용하는 Game Object에 추가된 시점을 의미합니다.)
        """
        super().Start()

    @abstractmethod
    def OnDestroy(self) -> None:
        """
        해당 Component가 파괴될 때 한번 실행됩니다.
        (※ 해당 Component를 관리하는 Controller/Manager로부터 삭제된 시점을 의미합니다. 완전한 삭제는 '가비지 컬렉터'에 의존합니다.)
        """
        super().OnDestroy()
    # endregion
