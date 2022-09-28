from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    A.sort()
    for i in range(len(A)):
        left, right = i, len(A) - 1
        while left <= right:
            if A[i] + A[left] + A[right] < t:
                left += 1
            elif A[i] + A[left] + A[right] > t:
                right -= 1
            else:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
