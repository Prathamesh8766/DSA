class Person:
    __name="o"

    def __helper(self):
        return self.__name

    def welcome(self):
        return self.__helper()

p=Person()
print(p.welcome())            


class Abc:
    def __init__(self, name, age):
        self._name = name
        self.age = age
        self._count = 0   # instance variable for count

    @property
    def name(self):
        return self._name

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value > 0:
            self._count += value


k = Abc("Doges", 89)
k.count = 4
print(f"{k.name}, {k.age}, {k.count}")
