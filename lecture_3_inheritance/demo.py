class Parent:
    def say_hi(self):
        return "Parent class says hello"

class FirstChild(Parent):
    pass
    # def say_hi(self):
    #     return "FirstChild class says hello"

class SecondChild(Parent):
    pass
    # def say_hi(self):
    #     return "SecondChild class says hello"

class GrandChild(FirstChild, SecondChild):
    pass


print(Parent.mro())
