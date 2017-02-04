import abc


class Building(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def report(self):
        """An abstract method template"""


class House(Building):

    def report(self):
        print(self)

    def __str__(self):
        attributes = ''
        attributes_values = dict(self.__dict__)
        for key in attributes_values:
            attributes += attributes_values[key]
        return 'House{}'.format(attributes)


class BuildingMaterialDecorator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_decorator(self, building):
        """An abstract method template"""


class BuildingMaterialBrickDecorator(BuildingMaterialDecorator):

    def add_decorator(self, building):
        building.material = ' made with brick;'


class BuildingColorDecorator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_decorator(self, building):
        """An abstract method template"""


class BuildingColorGreenDecorator(BuildingColorDecorator):

    def add_decorator(self, building):
        building.color = ' with green facade;'


class BuildingRoofFormDecorator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def add_decorator(self, building):
        """An abstract method template"""


class BuildingRoofFormTriangleDecorator(BuildingColorDecorator):

    def add_decorator(self, building):
        building.roof_form = ' with triangle roof form;'


house = House()

material_brick = BuildingMaterialBrickDecorator()
material_brick.add_decorator(house)

color_green = BuildingColorGreenDecorator()
color_green.add_decorator(house)

roof_form_triangle = BuildingRoofFormTriangleDecorator()
roof_form_triangle.add_decorator(house)

print(house)
