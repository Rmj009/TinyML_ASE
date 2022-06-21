from tokenize import Single


class Singleton1(object):
    """insantiate singleton"""
    _instance = None
    _isFirstInit = False
    def __new__(cls, name):
        if not cls._instance:
            Singleton1._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,name) -> None:
        if not self._isFirstInit:
            self._name = name
            Singleton1._isFirstInit = True
    
    def getName(self):
        return self._name


### caseTest
tony = Singleton1("Tony")
karry = Singleton1("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(Karry):", id(karry))
print("tony == karry: ", tony == karry)