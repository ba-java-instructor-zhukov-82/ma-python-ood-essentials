class A:

    def __init__(self, a):
        self.__a = a
        self._common = 'A common'

    def method(self):
        print('class A:', self.__a)


class B:

    def __init__(self, b):
        self.__b = b
        self._common = 'B common'

    def method(self):
        print('class B:', self.__b)


class C(A, B):

    def __init__(self, a, b, c):
        A.__init__(self, a)
        B.__init__(self, b)
        self.__c = c

    def method(self):
        print('class C:', self.__c)

    def test_super_methods(self):
        A.method(self)
        B.method(self)
        self.method()

    def test_distinct_attributes(self):
        print(A.__getattribute__(self, '_A__a'))
        print(B.__getattribute__(self, '_B__b'))

    def test_shared_attributes(self):
        print(super(A, self).__getattribute__('_common'))
        print(super(B, self).__getattribute__('_common'))


c = C('a', 'b', 'c')
# c.test_super_methods()
# c.test_distinct_attributes()
c.test_shared_attributes()