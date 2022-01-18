from unittest import TestCase

from _pytest.fixtures import fixture
from _pytest.python_api import raises

from solver import Solver


class CalculatorTestCase(TestCase):
    def setUp(self):
        self.solver = Solver(2, 6)

    def test_add(self):
        # solver = Solver(2, 6)
        result = self.solver.add()
        self.assertEqual(result, 8)

    def test_multiply(self):
        # solver = Solver(2, 1)
        result = self.solver.multiply()
        self.assertEqual(result, 12)


@fixture
def solver_instance():
    solver = Solver(6, 2)
    return solver


@fixture
def faulty_instance():
    solver = Solver(2, 0)
    return solver


class TestCalculator:

    def test_add(self, solver_instance):
        result = solver_instance.add()
        assert result == 8

    def test_multiply(self, solver_instance):
        result = solver_instance.multiply()
        assert result == 12

    def test_divide(self, solver_instance):
        result = solver_instance.divide()
        assert result == 3

    def test_divide__raises(self, faulty_instance):
        with raises(ZeroDivisionError) as ex:
            faulty_instance.divide()
        assert str(ex.value) == "you can not divide by 0"


def test_add():
    solver = Solver(2, 3)
    assert solver.add() == 5
