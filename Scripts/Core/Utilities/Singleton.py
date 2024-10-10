from typing import Any, Dict, Type, ClassVar
from threading import Lock

class Singleton(type):
    __instances: ClassVar[Dict[Type[Any], Any]] = {}
    __lock: ClassVar[Lock]                      = Lock()  # 스레드 안전성을 위한 락 추가

    def __call__(cls, *args, **kwargs) -> Any:
        # 인스턴스 생성 시 스레드 안전성 보장
        with cls.__lock:
            if cls not in cls.__instances:
                cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]