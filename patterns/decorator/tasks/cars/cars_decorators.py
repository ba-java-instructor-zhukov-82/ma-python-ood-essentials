import abc


class Car(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def report(self):
        """An abstract method template"""


class BMW(Car):

    def report(self):
        print(self)

    def __str__(self):
        return 'BMW'


class Mazda(Car):

    def report(self):
        print(self)

    def __str__(self):
        return 'Mazda'


class CarBodyDecorator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def report(self, car):
        """An abstract method template"""


