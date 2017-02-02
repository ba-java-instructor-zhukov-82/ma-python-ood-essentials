import abc


class Eater(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def eat(self):
            """Pseudo abstract method that imitate reference behavior"""


class Person(Eater):

    def eat(self):
        print('Person is eating...')


class Health:
    SICK = 'sick'
    EMPLOYABLE = 'employable'
    HORSE = 'horse'

    def __init__(self, health_level):
        self.health_level = health_level

    def __str__(self):
        return '\thealth: {}\n'.format(self.health_level)


class Tools:

    def __init__(self, *tools_list):
        self.tools_list = tools_list

    def __str__(self):
        return '\ttools: {}\n'.format(self.tools_list)


class Worker(Eater):
    def __init__(self, health, tools):
        self._health = health
        self.tools = tools

    def eat(self):
        print('Worker is eating...')

    def __str__(self):
        return 'Worker:\n {} {}'.format(self._health.__str__(), self.tools.__str__())


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


def eat_test():
    person = Person()
    worker = Worker()
    do_eat([person, worker])

# eat_test()


def composition_test():
    worker_horse = Worker(Health(Health.HORSE))
    print(worker_horse)

# composition_test()

def aggregation_test():
    worker_equipped = Worker(Health(Health.EMPLOYABLE), Tools('nails', 'hummer'))
    print(worker_equipped)

aggregation_test()
