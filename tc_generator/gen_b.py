""" gen_a generate the tests cases for the problem b"""
from random import randint
from solutions.b import solution

from string import ascii_lowercase as al


def generate_string(size: int) -> str:
    """ generate a random ab string of size length"""
    return ''.join(al[randint(0, len(al) - 1)] for _ in range(size))


def generate_test_cases_sol_b(path) -> None:
    """ given a path generate the tests cases for the problem a """
    n_tests = 1000
    size_input = 10 ** 4
    with open(path, "w", encoding="UTF-8") as file:
        for _ in range(n_tests):
            size_test = randint(size_input / n_tests, size_input)
            input_3_lines = list(generate_string(size_test) for _ in range(3))
            input_3_lines += list(map(str, solution(input_3_lines)))
            file.write(f"{' '.join(input_3_lines)}\n")
