from abc import ABCMeta
from typing import final, List, Dict, Type, TypeVar, Sequence

from Core.Components.Component import Component
from Core.Components.GameObject import GameObject

class Behavior(Component, metaclass = ABCMeta):
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

# 타입 검색을 위한 제너릭 타입 선언.
TBehavior: TypeVar = TypeVar('TBehavior', bound = Behavior)

@final
class BehaviorManager:
    def __init__(self, _actor: GameObject):
        self.__actor: GameObject                                = _actor    # 행동 수행자
        self.__behaviors: Dict[Type[TBehavior], Behavior]       = {}        # 행동
        self.__addBehaviors: Dict[Type[TBehavior], Behavior]    = {}        # 추가될 행동

    def AddBehavior(self, _behaviorType: Type[TBehavior]) -> TBehavior:
        if _behaviorType in self.__behaviors:
            raise ValueError(f"[Oops!] 중복된 Behavior는 허용하지 않습니다! {type(_behaviorType)}")

        newBehavior: TBehavior = _behaviorType(self.__actor)
        newBehavior.Start()
        newBehavior.OnEnable()
        self.__addBehaviors[_behaviorType] = newBehavior

        return newBehavior

    def AddBehaviors(self, *_behaviorTypes: Type[TBehavior]) -> Sequence[TBehavior]:
        newBehaviors: List[TBehavior] = []
        for currentBehavior in self.__behaviors:
            if currentBehavior in self.__behaviors:
                raise ValueError(f"[Oops!] 중복된 Behavior는 허용하지 않습니다! {type(currentBehavior)}")

            newBehavior: TBehavior = currentBehavior(self.__actor)
            newBehavior.Start()
            newBehavior.OnEnable()
            self.__addBehaviors[currentBehavior] = newBehavior
            newBehaviors.append(currentBehavior(self.__actor))

        return newBehaviors

    def RemoveBehavior(self, _behaviorType: Type[TBehavior]) -> bool:
        if _behaviorType not in self.__behaviors:
            return False

        self.__behaviors.pop(_behaviorType)
        return True

    def RemoveBehaviors(self, *_behaviors: Type[TBehavior]) -> bool:
        condition = False
        for behavior in _behaviors:
            if behavior in self.__behaviors:
                self.__behaviors.pop(behavior)
                condition = True

        return condition

    def GetBehavior(self, _behaviorType: Type[TBehavior]) -> TBehavior:
        return self.__behaviors[_behaviorType] if _behaviorType in self.__behaviors else None

    def GetBehaviors(self, *_behaviorTypes: Type[TBehavior]) -> Sequence[TBehavior]:
        return [self.__behaviors[behaviorType] for behaviorType in _behaviorTypes if behaviorType in self.__behaviors]

    def Update(self, _deltaTime):
        if len(self.__addBehaviors) > 0:
            self.__behaviors.update(self.__addBehaviors)

        if len(self.__behaviors) > 0:
            for behavior in self.__behaviors:
                if behavior.isEnable:
                    behavior.Update(_deltaTime)

        if len(self.__behaviors) > 0:
            for behavior in self.__behaviors:
                if behavior.isEnable:
                    behavior.LateUpdate(_deltaTime)

    def FixedUpdate(self, _fixedDeltaTime):
        if len(self.__behaviors) > 0:
            for behavior in self.__behaviors:
                if behavior.isEnable:
                    behavior.FixedUpdate(_fixedDeltaTime)

                if behavior.isDestroy:
                    key: Type[TBehavior] = next(key for key, value in self.__behaviors.items() if value is behavior)
                    self.__behaviors.pop(key).OnDestroy()
