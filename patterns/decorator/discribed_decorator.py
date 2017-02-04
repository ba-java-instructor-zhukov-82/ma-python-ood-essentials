def described_decorator(description):
    def wrapper(func):
        print(description)
        return func
    return wrapper


def arg_multiple(value):
    def wrapper(func):
        def receiver(*args):
            return func(*(list(map(lambda x: x * value, args))))
        return receiver
    return wrapper



@described_decorator(description='\tdecorator')
def test():
    print('test')


@arg_multiple(value=5)
def add(a, b):
    return a + b


test()
print(add(5, 10))