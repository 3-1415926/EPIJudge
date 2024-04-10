from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def recursive_permutations(index: int):
        if index >= len(A) - 1:
            results.append(A.copy())
            return
        for i in range(index, len(A)):
            A[index], A[i] = A[i], A[index]
            recursive_permutations(index + 1)
        for i in range((len(A) - index) // 2):
            A[index + i], A[len(A) + ~i] = A[len(A) + ~i], A[index + i]
            
    results = []
    recursive_permutations(0)
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
