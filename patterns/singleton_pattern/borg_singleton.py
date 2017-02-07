class Borg(object):
    __shared_state = {'key': 'value'}

    def __get_state(cls):
        return cls.__shared_state

    def __set_state(cls, new_state):
        cls.__shared_state = new_state

    state = property(__get_state, __set_state)

    def update(cls, key, value):
        if key in cls.__shared_state:
            cls.__shared_state[key] = value

    def put(cls, key, value):
        if key not in cls.__shared_state:
            cls.__shared_state[key] = value

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

    def print_shared(self):
        print(self.__shared_state)


borg = Borg()
borg2 = Borg()

print(borg.__dict__)
# borg.state = {'key2': 'value2'}
# print(borg.__dict__)
borg.update('key', 'value updated')
print(borg.__dict__)
borg.put('key2', 'value2')
print(borg.__dict__)
print(borg2.__dict__)
