from abc import ABCMeta

from GUI.UIObject import UIObject
from GUI.ETransitionState import ETransitionState

class BaseTransition(metaclass = ABCMeta, UIObject):
    def __init__(self):
        super().__init__()
        
        self._isExitAfterEnter: bool = True
        self._isPlaying: bool = True
        self._currentState: ETransitionState = ETransitionState.IDLE

    def Start(self) -> None:
        self._isPlaying = False
        self._currentState = ETransitionState.IDLE

    def Update(self, _deltaTime: float) -> None:
        if self._isPlaying:
            self.UpdateOnPlaying()

    # -------------------[virtual methods]------------------- #

    def Enter(self) -> None:
        self.isActive = True
        self._currentState = ETransitionState.ENTER

    def EnterComplete(self) -> None:
        if self._isExitAfterEnter:
            self.Exit()
            return

        self._currentState = ETransitionState.ENTERCOMPLETE

    def Exit(self) -> None:
        self.isActive = True
        self._currentState = ETransitionState.EXIT

    def ExitComplete(self) -> None:
        self._currentState = ETransitionState.EXITCOMPLETE

    def Play(self) -> None:
        self.isActive = True
        self._isPlaying = True

    def Pause(self) -> None:
        self._isPlaying = False

    def Stop(self) -> None:
        self._currentState = ETransitionState.ENTER

    def UpdateOnPlaying(self) -> None:
        pass