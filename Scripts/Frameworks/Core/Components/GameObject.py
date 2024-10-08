from typing import final

from Core.Components.Object import Object

class GameObject(Object):
    def __init__(self):
        super().__init__()

        from Core.Components.Component import ComponentManager
        from Core.Components.Transform import Transform

        self.__componentManager: ComponentManager = ComponentManager(self)
        self.__componentManager.AddComponent(Transform)

    #region [Properties]
    @property
    def transform(self) -> 'Transform':
        from Core.Components.Transform import Transform
        return self.__componentManager.GetComponent(Transform)

    @property
    def gameObject(self) -> 'GameObject':
        return self
    #endregion

@final
class GameObjectManager:
    def __init__(self):
        pass
