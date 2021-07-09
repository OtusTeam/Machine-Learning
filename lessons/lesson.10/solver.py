class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        print("a", self.a, "+", "b", self.b, "=", result)
        return result

    def mul(self):
        # return self.a * self.b
        return mul(self.a, self.b)


def mul(a, b):
    return a * b
