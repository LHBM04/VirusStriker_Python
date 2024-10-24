from abc import ABCMeta, abstractmethod

from Core.Objects.Object import Object

class ScriptableObject(Object, metaclass = ABCMeta):
    @abstractmethod
    def ToJson(self):
        ...

    @abstractmethod
    def FromJson(self):
        ...


