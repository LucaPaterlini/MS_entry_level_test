import os
from typing import List, Callable


def file_to_test(filepath: str, generator: Callable[[str], None]) -> List[List[str]]:
    """ reads a file and prepares the test cases for the test"""
    if not os.path.exists(filepath):
        generator(filepath)
    count = 0
    with open(filepath, 'r', encoding="UTF-8") as file:
        return [[str(count)] + line.rstrip('\n').split(' ') for line in file]