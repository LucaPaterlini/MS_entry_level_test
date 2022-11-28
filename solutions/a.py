""" solution_a"""
import re


def default_solution(sequence: str) -> int:
    """uses regex to split the string in its substrings of the same type of characters
     and map each of them their length, as last step multiply the size of the sub strings
     for the max and subtract the length of the original string
    """
    tmp_vector = re.findall(r"a+", sequence)
    tmp_vector += re.findall(r"b+", sequence)
    tmp_vector = list(map(len, tmp_vector))
    max_substring_length = max(tmp_vector)
    return max_substring_length * len(tmp_vector) - len(sequence)


def solution(sequence: str) -> int:
    """returns how many characters have to be added to make each a or b subsection
     evenly balanced in its subsequences
    """
    previous_character = sequence[0]
    counter = 1
    n_chunks = 1
    max_len_chunks = 0
    for current_character in sequence[1:]:
        if current_character != previous_character:
            max_len_chunks = max(max_len_chunks, counter)
            counter = 0
            n_chunks += 1
        previous_character = current_character
        counter += 1
    max_len_chunks = max(max_len_chunks, counter)
    return round((max_len_chunks - len(sequence) / n_chunks) * n_chunks)


def solution_indexes(sequence: str) -> int:
    """similar to the previous solution but instead of copying the item of the array
    and executing on them individually I have used reference instead
    """
    counter = 1
    n_chunks = 1
    max_len_chunks = 0
    for i in range(1, len(sequence)):
        if sequence[i - 1] != sequence[i]:
            max_len_chunks = max(max_len_chunks, counter)
            counter = 0
            n_chunks += 1
        counter += 1
    max_len_chunks = max(max_len_chunks, counter)
    return round((max_len_chunks - len(sequence) / n_chunks) * n_chunks)
