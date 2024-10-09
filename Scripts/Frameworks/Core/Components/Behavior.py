from Core.Components.Component import Component

class Behavior(Component):
    def __init__(self, _actor: 'GameObject'):
        from Core.Components.GameObject import GameObject

        super().__init__(_actor)

        self.__actor: GameObject    = _actor
        self.__isEnable: bool       = True

    # region [Properties]
    @property
    def isEnable(self) -> bool:
        return self.__isEnable

    @isEnable.setter
    def isEnable(self, _enable) -> None:
        if _enable:
            self.__isEnable = True
            self.OnEnable()
        else:
            self.__isEnable = False
            self.OnDisable()
    # endregion
    # region [Life-Cycle Methods]
    def OnEnable(self) -> None:
        pass

    def Update(self, _deltaTime: float):
        pass

    def FixedUpdate(self, _fixedDeltaTime: float):
        pass

    def LateUpdate(self, _deltaTime: float):
        pass

    def OnDisable(self) -> None:
        pass
    # endregion