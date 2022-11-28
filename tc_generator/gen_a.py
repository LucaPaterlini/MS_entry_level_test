""" gen_a generate the tests cases for the problem a"""
from random import randint
from solutions.a import default_solution


def generate_string(size: int) -> str:
    """ generate a random ab string of size length"""
    return ''.join('ab'[randint(0, 1)] for _ in range(size))


def generate_test_cases_sol_a(path) -> None:
    """ given a path generate the tests cases for the problem a """
    n_tests = 100
    size_input = 10 ** 5
    with open(path, "w", encoding="UTF-8") as file:
        for _ in range(n_tests):
            test_case = generate_string(randint(size_input / n_tests, size_input))
            file.write(f"{test_case} {default_solution(test_case)}\n")
