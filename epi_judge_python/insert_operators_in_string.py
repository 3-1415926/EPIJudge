from functools import cache
from traceback import print_exc
from typing import List, Set

from test_framework import generic_test

def expression_synthesis(digits: List[int], target: int) -> bool:
    @cache
    def find_cat_value(start: int, end: int, *, base: int) -> int:
        if start >= end: return base
        return find_cat_value(start, end - 1, base=0) * 10 + digits[end - 1]

    @cache
    def find_mul_values(start: int, end: int, base: int) -> Set[int]:
        if start >= end: return {base}
        return {find_cat_value(start, i, base=1) * mv for i in range(start + 1, end + 1) for mv in find_mul_values(i, end, base=1)}

    @cache
    def find_add_values(start: int, end: int, base: int) -> Set[int]:
        if start >= end: return {base}
        return {(mv + av) for i in range(start + 1, end + 1) for mv in find_mul_values(start, i, base=0) for av in find_add_values(i, end, base=0)}

    try:
        return target in find_add_values(0, len(digits), base=0)
    except TypeError:
        print_exc()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('insert_operators_in_string.py',
                                       'insert_operators_in_string.tsv',
                                       expression_synthesis))
