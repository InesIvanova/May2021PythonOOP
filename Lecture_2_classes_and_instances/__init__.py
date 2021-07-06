class Vehicle(object):
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []

    def move(self, m):
        self.mileage += m
        print("Moving...")

    # def __str__(self):
    #     return f"This a vehicle with max speed {self.max_speed} and mileages {self.mileage}"

    def __repr__(self):
        return "asd"


v = Vehicle(20)

v2 = Vehicle(20)
v.mileage = 100000000
v.brand = "Hello"
print(v2.brand)


