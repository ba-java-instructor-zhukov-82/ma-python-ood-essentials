class PropertySource:

    def __init__(self, attribute):
        self.__attribute = attribute

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def set_attribute(self, attribute):
        self.__attribute = attribute

    @attribute.deleter
    def del_attribute(self):
        del self.__attribute


test = PropertySource('attribute')
print(test.attribute)
# test.attribute = 'new attribute'
# print(test.attribute)
