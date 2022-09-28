from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    A.sort()
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] < t:
            i += 1
        elif A[i] + A[j] > t:
            j -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
