# return for each triple the first position where the character is common for each of them
from typing import List


def solution(three_strings: List[str]):
    """ given an array of 3 strings of the same length find the first common
     letter and its 3 positions in the strings"""
    tmp_mem = [[-1] * 26 for _ in range(4)]
    for i in range(len(three_strings[0])):
        for j in range(3):
            letter_pos = ord(three_strings[j][i]) - ord('a')
            if tmp_mem[j][letter_pos] == -1:
                tmp_mem[j][letter_pos] = i
                tmp_mem[3][letter_pos] += 1
                if tmp_mem[3][letter_pos] == 2:
                    return tuple(tmp_mem[j][letter_pos] for j in range(3))


if __name__ == '__main__':
    print(solution(["abc", "bca", "dbe"]))
    print(solution(["ba", "za", "ca"]))
