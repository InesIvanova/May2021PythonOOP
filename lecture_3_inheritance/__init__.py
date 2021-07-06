class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Age can not be negative")
        return age

    def sleep(self):
        return "I am sleeping"

    def __repr__(self):
        return "This is a person"


class Employee(Person):
    def __init__(self, name, age, date):
        super().__init__(name, age)
        self.date = date

    def work(self):
        return "working"

    def __repr__(self):
        return super().__repr__() + " who is also a Employee"



e = Employee("test", 5, "...")
print(e.sleep())




class Manager(Person):
    def __init__(self, name, age, people_managing):
        super().__init__(name, age)
        self.people_managing = people_managing



class Contractor(Person):
    def __init__(self, name, age, date_of_expiry):
        super().__init__(name, age)
        self.date_of_expiry = date_of_expiry
