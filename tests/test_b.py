import timeit
import unittest

from parameterized import parameterized

from solutions.b import solution
from tc_generator.gen_b import generate_test_cases_sol_b
from tc_generator.helpers import file_to_test

FUNCTIONS_TO_TEST = (solution,)
FILE_TEST_CASES = './test_cases/testB.txt'


class TestProblemB(unittest.TestCase):
    """ Contains all the test for the problem a"""

    @parameterized.expand(file_to_test(FILE_TEST_CASES,generate_test_cases_sol_b))
    def test_sequence(self, pos: str, *input_seq: str):
        """ test all the test cases for each of the proposed solution """
        for function_to_test in FUNCTIONS_TO_TEST:
            got = function_to_test(list(input_seq[:3]))
            self.assertEqual(got, tuple(map(int, input_seq[3:])), f"Test#{pos}: {function_to_test.__name__}")

    def test_bench_sequence(self):
        """ test time performance of all the proposed solutions """
        data = file_to_test(FILE_TEST_CASES, generate_test_cases_sol_b)
        perf = []
        for function_to_test in FUNCTIONS_TO_TEST:
            perf.append((timeit.timeit(
                lambda local_f=function_to_test: list((local_f(input_line[1:4])
                                                       for input_line in data)), number=100),
                         function_to_test.__name__))
        self.assertEqual(min(perf)[1], FUNCTIONS_TO_TEST[0].__name__, perf)
