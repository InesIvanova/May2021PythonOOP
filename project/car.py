from project.vehicle import Vehicle


class Car(Vehicle):
    def drive(self) -> str:
        return "driving..."