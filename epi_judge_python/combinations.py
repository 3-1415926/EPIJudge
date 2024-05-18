from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    combination = [i < k for i in range(n)]
    make_combination = lambda: [(i + 1) for i, x in enumerate(combination) if x]
    results = [make_combination()]
    while True:
        i = n - 1
        while i > 0 and (not combination[i - 1] or combination[i]):
            i -= 1
        if i <= 0:
            break
        combination[i - 1], combination[i] = combination[i], combination[i - 1]
        i, j = i + 1, n - 1
        while i < j:
            combination[i], combination[j] = combination[j], combination[i]
            i += 1
            j -= 1
        results.append(make_combination())
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
