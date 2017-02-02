import abc


class Eater(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def eat(self):
            """Pseudo abstract method that imitate reference behavior"""


class Person(Eater):

    def eat(self):
        print('Person is eating...')


class Worker(Eater):

    def eat(self):
        print('Worker is eating...')


def do_eat(eaters):
    for eater in eaters:
        eater.eat()


def do_eat_single(eater):
    eater.eat()

try:
    eater = Eater()
    eater.eat()
except Exception:
    print('Interface type can not be instantiated!')


person = Person()
worker = Worker()
do_eat([person, worker])
