class CoordinateSystem:

    C_2D = 'C_2D'
    C_3D = 'C_3D'


class Point2D:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y


class Point3D:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z


class Coordinates(Point2D, Point3D):

    def __init__(self, c_system, *args):
        if c_system == CoordinateSystem.C_2D:
            Point2D.__init__(self, *args)
        elif c_system == CoordinateSystem.C_3D:
            Point3D.__init__(self, *args)
        else:
            print('Incorrect values passed!')
        self.__c_system = c_system


    def change_system(self, vector):
        if self.__c_system == CoordinateSystem.C_2D:
            Point3D.__init__(self, self._Point2D__x + vector,
                             self._Point2D__y + vector, vector)
            self._Point2D__x = None
            self._Point2D__y = None
            self.__c_system = CoordinateSystem.C_3D
        else:
            Point2D.__init__(self, self._Point3D__x + vector,
                             self._Point3D__y + vector)
            self._Point3D__x = None
            self._Point3D__y = None
            self._Point3D__z = None
            self.__c_system = CoordinateSystem.C_3D

    def __str__(self):
        to_str = None
        if self.__c_system == CoordinateSystem.C_3D:
            return 'Coordinates:\n\tx: {}\n\ty: {}\n\tz: {}\n'\
            .format(self._Point3D__x, self._Point3D__y, self._Point3D__z)
        else:
            return 'Coordinates:\n\tx: {}\n\ty: {}\n' \
                .format(self._Point2D__x, self._Point2D__y)


point = Coordinates(CoordinateSystem.C_2D, 5, 10)
print(point)
point.change_system(5)
print(point)
