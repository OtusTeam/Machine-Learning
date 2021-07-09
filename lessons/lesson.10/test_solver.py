from unittest import TestCase

import pytest
from pytest import fixture

from solver import Solver, mul


@fixture
def solver_instance():
    return Solver(7, 9)


@fixture
def solver_eq(solver_instance):
    solver_instance.a = solver_instance.b
    return solver_instance


class TestSolverUnittest(TestCase):

    def test_add(self):
        s = Solver(5, 10)
        res = s.add()
        self.assertEqual(15, res)

    def test_add_equal(self):
        s = Solver(15, 15)
        res = s.add()
        self.assertEqual(30, res)


class TestSolver:

    def test_add(self, solver_instance):
        res = solver_instance.add()
        assert res == solver_instance.a + solver_instance.b

    def test_add_equal(self, solver_eq):
        assert solver_eq.a == solver_eq.b
        res = solver_eq.add()
        assert res == solver_eq.a + solver_eq.b

    def test_mul(self, solver_instance):
        res = solver_instance.mul()
        assert res == solver_instance.a * solver_instance.b

    @pytest.mark.parametrize("a, b, expected_result", [
        [1, 2, 3],
        [10, 10, 20],
        [5, 7, 12],
        pytest.param(
            6, 9, 15,
            id="add-6-9-get-15",
        ),
    ])
    def test_add_many(self, a, b, expected_result):
        s = Solver(a, b)
        res = s.add()
        assert res == expected_result


def test_mul():
    res = mul(8, 5)
    assert res == 40
