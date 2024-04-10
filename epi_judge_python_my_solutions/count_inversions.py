from typing import List

from test_framework import generic_test


def count_inversions(A: List[int]) -> int:
    def recursive_inversions(start: int, end: int):
        if start + 1 >= end: return 0
        mid = (start + end) // 2
        count = recursive_inversions(start, mid) + recursive_inversions(mid, end)
        i, j = start, mid
        for t in range(start, end):
            if i < mid and (j >= end or A[i] <= A[j]):
                B[t] = A[i]
                i += 1
            else:
                B[t] = A[j]
                j += 1
                count += mid - i
        for t in range(start, end):
            A[t] = B[t]
        return count
    B = [None] * len(A)
    return recursive_inversions(0, len(A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_inversions.py',
                                       'count_inversions.tsv',
                                       count_inversions))
