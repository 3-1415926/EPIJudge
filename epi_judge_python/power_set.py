from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def recursive_power_set(start: int):
        if start >= len(input_set):
            results.append(cur_set.copy())
            return
        recursive_power_set(start + 1)
        cur_set.append(input_set[start])
        recursive_power_set(start + 1)
        cur_set.pop()
    cur_set = []
    results = []
    recursive_power_set(0)
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
