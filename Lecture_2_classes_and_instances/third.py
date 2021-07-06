class Circle:
    """
    This class is responsible for creating a circle.
    Gicles the ability to set new radius and provide some arithmetical
    calculations such as area....
    """
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_r):
        """
        This methods sets new value for the circle's radius
        :param new_r: this will be the new value of the circle's radius
        """
        self.radius = new_r

    def get_area(self):
        return Circle.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


print(Circle.__doc__)
