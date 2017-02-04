# decorator for procedure template: takes one argument and return None


# procedure decorator
def procedure_decorator(func):
    def wrapper(data):
        return func(str(data).upper())
    return wrapper


# procedure itself
@procedure_decorator
def printer(data):
    print(data)


printer('test')

# --------------------------------------------------------------------------------

# decorator for operation that takes two arguments and returns some not None value


# operation decorator
def operation_decorator(func):
    def wrapper(a, b):
        return func(a * a, b * b)
    return wrapper


# operation itself
@operation_decorator
def operation(a, b):
    return a + b


print(operation(5, 10))

# ---------------------------------------------------------------------------------

# decorator with variable arguments


# operation decorator
def vargs_decorator(func):
    def wrapper(*args):
        return func(*(list(map(lambda x: x * x, args))))
    return wrapper


# operation with one argument
@vargs_decorator
def increment(a):
    print('increment')
    return a + 1


# operation with two argument
@vargs_decorator
def add(a, b):
    print('add')
    return a + b


# operation with two argument
@vargs_decorator
def sum_of_three(a, b, c):
    print('sum of three')
    return a + b + c


print(increment(10))
print(add(10, 20))
print(sum_of_three(10, 20, 30))
