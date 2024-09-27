class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class LazySingleton:
    m_instance = None
    def __init__(self):
        if not self.m_instance:
            print("instance None")
        else:
            print(f"instance {self.GetInstance()}")
 
    @classmethod
    def GetInstance(cls):
        if not cls.m_instance:
            cls.m_instance = LazySingleton()
        return cls.m_instance