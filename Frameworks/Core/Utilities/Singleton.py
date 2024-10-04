from abc import ABCMeta

class Singleton(metaclass = ABCMeta, type):
    __instances: 'Singleton' = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]