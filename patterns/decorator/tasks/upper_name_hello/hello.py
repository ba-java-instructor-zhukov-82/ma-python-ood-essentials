# name to upper case decorator
def upper(func):
    def wrapper():
        return str(func()).upper()
    return wrapper


# name reader from input stream
@upper
def read_name():
    return input('Please, enter your name:')


# hello function with name defined user
def hello():
    print('Hello, {}!'.format(read_name()))

hello()
