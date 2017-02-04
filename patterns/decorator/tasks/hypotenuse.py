from math import sqrt

def sum(func):
    def wrapper():
        def result():
            return func() + func()
        return result
    return wrapper()


def square(func):
    def wrapper():
        def power():
            base = func()
            return base * base
        return power
    return wrapper()


def root(func):
    def wrapper():
        return sqrt(func())
    return wrapper

def cathetus():
    try:
        return float(input('Please, enter the cathetus:'))
    except ValueError:
        return 0.0


@root
@sum
@square
def hypotenuse():
    return cathetus()


print(hypotenuse())
