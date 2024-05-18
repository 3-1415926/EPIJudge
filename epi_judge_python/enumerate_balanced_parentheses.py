from functools import cache
from typing import List

from test_framework import generic_test, test_utils

@cache
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    if num_pairs == 0: return [""]
    if num_pairs == 1: return ["()"]
    results = []
    for split in range(num_pairs):
        for a in generate_balanced_parentheses(split):
            for b in generate_balanced_parentheses(num_pairs - split - 1):
                results.append(f"({a}){b}")
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
