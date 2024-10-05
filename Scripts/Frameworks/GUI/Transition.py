from Core.Components.Animation.Animator import Animator
from GUI.BaseTransition import BaseTransition


class Transition(BaseTransition):
    def __init__(self):
        super().__init__()

        self._animator: Animator = None