from abc import ABC
import exceptions

class Vehicle(ABC):
    def __init__(self, started, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, dist_km):
        fuel_to_move = dist_km * self.fuel_consumption
        if self.fuel >= fuel_to_move:
            self.fuel = self.fuel - fuel_to_move

        else:
            raise exceptions.NotEnoughFuel