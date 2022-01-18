class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("you can not divide by 0")
        return self.a / self.b


if __name__ == "__main__":
    solver = Solver(2, 5)
    print(solver.add() == 7)
