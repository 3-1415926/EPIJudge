from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    def recursive_parentheses(start: int, end: int):
        if start >= end:
            yield
            return
        cur_result[start] = '('
        for i in range(start + 1, end, 2):
            cur_result[i] = ')'
            for _ in recursive_parentheses(start + 1, i):
                for _ in recursive_parentheses(i + 1, end):
                    yield
    cur_result = ['#'] * (num_pairs * 2)
    results = []
    for _ in recursive_parentheses(0, num_pairs * 2):
        results.append(''.join(cur_result))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
