from collections import Counter
from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    results = [[]]
    if not input_set:
        return results
    elements, max_counts = map(list, zip(*sorted(Counter(input_set).items())))
    cur_counts = [0] * len(elements)
    while True:
        i = len(elements) - 1
        while i >= 0 and cur_counts[i] >= max_counts[i]:
            i -= 1
        if i < 0:
            break
        cur_counts[i] += 1
        i += 1
        while i < len(elements):
            cur_counts[i] = 0
            i += 1
        results.append([elements[i] for i in range(len(elements)) for _ in range(cur_counts[i])])
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
