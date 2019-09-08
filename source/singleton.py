"""This source code demonstrate examples of singleton design pattern"""


class SingletonMetaClass(type):
    """
    This is Metaclass to define the behavior of a sungleton class
    """
    _instances_dict = {}

    def __call__(cls, *args, **kwargs):
        print(cls._instances_dict)
        if not cls._instances_dict.get(cls):
            cls._instances_dict[cls] = super(SingletonMetaClass, cls).\
                __call__(*args,**kwargs)
        return cls._instances_dict[cls]


class ConnectionClass1(metaclass=SingletonMetaClass):
    """
    This is a dummy connection class
    """
    def __init__(self):
        print(f"Initiating a class of type {type(self)}")
        self._connection_string = "ConnectionClass1"

    @property
    def get_connection_string(self):
        return self._connection_string


class ConnectionClass2(metaclass=SingletonMetaClass):
    """
    This is a dummy connection class
    """
    def __init__(self):
        print(f"Initiating a class of type {type(self)}")
        self._connection_string = "ConnectionClass2"

    @property
    def get_connection_string(self):
        return self._connection_string


if __name__ == "__main__":
    print(ConnectionClass1() is ConnectionClass1())
    print(ConnectionClass2() is ConnectionClass2())
