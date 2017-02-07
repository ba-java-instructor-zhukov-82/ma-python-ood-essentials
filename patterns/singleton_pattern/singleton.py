class Singleton(object):

    def get_instance(cls):
        return cls.instance.__dict__

    def update(cls, key, value):
        if key in cls.instance.__dict__:
            cls.instance.__dict__[key] = value

    def put(cls, key, value):
        if key not in cls.instance.__dict__:
            cls.instance.__dict__[key] = value

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


singleton = Singleton()
another_singleton = Singleton()
print(singleton is another_singleton)
print(singleton.get_instance())
singleton.put('key', 'value')
print(singleton.get_instance())
singleton.update('key', 'value updated')
print(singleton.get_instance())
singleton.put('key2', 'value')
print(singleton.get_instance())
