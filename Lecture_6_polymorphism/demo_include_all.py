from abc import ABC, abstractmethod


#Abstraction
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    # encapslation
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 chars")
        self.__name = value

    @abstractmethod
    def sound(self, a):
        pass


class Cat(Animal):
    def sound(self):
        return "Meow"


# inheritance (common validators)
class Dog(Animal):
    def sound(self):
        return "Bau"


# Polymorphism
for animal in Cat("Sharo"), Dog("Oras"):
    print(animal.sound())