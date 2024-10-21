from typing import Any, Dict, Type, ClassVar
from threading import Lock

class Singleton(type):
    __instances: ClassVar[Dict[Type[Any], Any]] = {}
    __lock: ClassVar[Lock]                      = Lock()

    def __call__(cls, *args, **kwargs) -> Any:
        with cls.__lock:
            if cls not in cls.__instances:
                cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
