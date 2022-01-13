import  Vehicle
import exceptions

class Plane(Vehicle.Vehicle):
    def __init__(self, max_cargo):
        super().__init__(max_cargo)
        self.max_cargo = max_cargo
        self.cargo = 10

    def load_cargo(self, num):
        cargo_total = self.cargo + num
        if self.max_cargo >= cargo_total:
            self.cargo = cargo_total
            print(cargo_total)
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before