from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for a in A:
        i, j = 0, len(A) - 1
        while i <= j:
            if a + A[i] + A[j] < t:
                i += 1
            elif a + A[i] + A[j] > t:
                j -= 1
            else:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
