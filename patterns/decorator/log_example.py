def log(func):
    def wrapper(*args):
        print('\t', func.__name__, 'function invoked')
        return func(*args)
    return wrapper


@log
def add(a, b):
    return a + b


@log
def hello(name):
    print('Hello,', name, '!')


print(add(5, 10))
hello('Yevhen')
