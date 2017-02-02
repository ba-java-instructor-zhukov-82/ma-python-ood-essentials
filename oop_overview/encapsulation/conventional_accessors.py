class PythonAccessorsTest:

    def __init__(self, protected, private):
        self._protected = protected
        self.__private = private

test = PythonAccessorsTest('protected', 'private')
print('_protected attribute: ', test._protected)
print('__private attribute: ', test._PythonAccessorsTest__private)
