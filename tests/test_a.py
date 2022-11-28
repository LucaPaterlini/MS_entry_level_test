""" test_a : the test cases for the sol a"""
import timeit
import unittest
from parameterized import parameterized

from tc_generator.gen_a import generate_test_cases_sol_a
from solutions.a import solution, solution_indexes, default_solution
from tc_generator.helpers import file_to_test

FUNCTIONS_TO_TEST = (solution, solution_indexes, default_solution,)
FILE_TEST_CASES = './test_cases/testA.txt'


class TestProblemA(unittest.TestCase):
    """ Contains all the test for the problem a"""

    @parameterized.expand(file_to_test(FILE_TEST_CASES, generate_test_cases_sol_a))
    def test_sequence(self, pos: str, input_seq: str, expected: str):
        """ test all the test cases for each of the proposed solution """
        for function_to_test in FUNCTIONS_TO_TEST:
            got = function_to_test(input_seq)
            self.assertEqual(got, int(expected), f"Test#{pos}: {function_to_test.__name__}")

    def test_bench_sequence(self):
        """ test time performance of all the proposed solutions """
        data = file_to_test(FILE_TEST_CASES, generate_test_cases_sol_a)
        perf = []
        for function_to_test in FUNCTIONS_TO_TEST:
            perf.append((timeit.timeit(
                lambda local_f=function_to_test: list((local_f(input_seq)
                                                       for _, input_seq, _ in data)), number=5),
                         function_to_test.__name__))
        self.assertEqual(min(perf)[1], FUNCTIONS_TO_TEST[-1].__name__, perf)
