from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    def recursive_combinations(start: int, remaining: int):
        if remaining <= 0:
            results.append(cur_combination.copy())
            return
        for i in range(start, n + 2 - remaining):
            cur_combination.append(i)
            recursive_combinations(i + 1, remaining - 1)
            cur_combination.pop()
    cur_combination = []
    results = []
    recursive_combinations(1, k)
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
