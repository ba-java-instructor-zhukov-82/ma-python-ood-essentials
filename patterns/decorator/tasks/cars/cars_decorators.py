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


class CarBodySedanDecorator(CarBodyDecorator):

    def report(self, car):
        print(car, 'sedan')


class CarBodyHatchbackDecorator(CarBodyDecorator):

    def report(self, car):
        print(car, 'hatchback')


bmw = BMW()
mazda = Mazda()

car_body_sedan_decorator = CarBodySedanDecorator()
car_body_hatchback_decorator = CarBodyHatchbackDecorator()

car_body_sedan_decorator.report(bmw)
car_body_hatchback_decorator.report(mazda)
