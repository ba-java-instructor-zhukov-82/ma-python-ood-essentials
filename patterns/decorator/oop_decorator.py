import abc


class Shape(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def draw(self):
        """An abstract method template"""


class Rectangle(Shape):

    def draw(self):
        print(self)

    def __str__(self):
        return 'Rectangle'


class Circle(Shape):

    def draw(self):
        print(self)

    def __str__(self):
        return 'Circle'


class ShapeColorDecorator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def draw(self, shape):
        """An abstract method template"""


class ShapeGreenDecorator(ShapeColorDecorator):

    def draw(self, shape):
        print('Green', shape)


class ShapeYellowDecorator(ShapeColorDecorator):

    def draw(self, shape):
        print('Yellow', shape)


rectangle = Rectangle()
green_rectangle = ShapeGreenDecorator()
green_rectangle.draw(rectangle)

circle = Circle()
yellow_circle = ShapeYellowDecorator()
yellow_circle.draw(circle)
