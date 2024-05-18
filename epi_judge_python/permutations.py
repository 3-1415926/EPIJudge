from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    A.sort()    
    results = [A.copy()]
    if len(A) < 2: return results
    while True:
        i = len(A) - 2
        while i >= 0 and A[i] >= A[i + 1]:
            i -= 1
        if i < 0:
            break
        j = i
        while j + 1 < len(A) and A[j + 1] > A[i]:
            j += 1
        A[i], A[j] = A[j], A[i]
        i, j = i + 1, len(A) - 1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        results.append(A.copy())
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
