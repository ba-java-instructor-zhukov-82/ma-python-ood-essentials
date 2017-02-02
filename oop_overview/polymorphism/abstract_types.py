import abc


class AbstractWalker(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def walk(self):
            """Pseudo abstract method that imitate reference behavior"""


class Person(AbstractWalker):

    def walk(self):
        print('Person is walking...')


class Animal(AbstractWalker):

    def walk(self):
        print('Animal is running...')


def do_walk(walkers):
    for walker in walkers:
        walker.walk()


def do_walk_single(walker):
    walker.walk()

try:
    abstract = AbstractWalker()
    abstract.walk()
except Exception:
    print('Abstraction class can not be instantiated!')

class Q:

    pass


person = Person()
animal = Animal()
do_walk([person, animal])
