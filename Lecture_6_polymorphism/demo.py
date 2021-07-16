class ReversedInt:
    def __init__(self, value_int):
        self.value_int = value_int

    def __add__(self, other):
        return self.value_int - other.value_int


a = {1, 2, 3, 2}
b = {4, 5}
print(a.difference(b))
print(a - b)
ri = ReversedInt(5)
ri_2 = ReversedInt(10)
print(ri + ri_2)
print(ri_2 + ri)

class Person:
    def __init__(self, age):
        self.age = age

    def __ge__(self, other):
        return self.age >= other.age

    def __gt__(self, other):
        return self.age > other.age

p = Person(2)
p_2 = Person(2)
print(p >= p_2)
print(p > p_2)