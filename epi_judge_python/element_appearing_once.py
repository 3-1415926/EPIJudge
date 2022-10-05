from typing import List

from test_framework import generic_test

# hi lo +x -> hi lo
#  0  0  0     0  0
#  0  0  1     0  1
#  0  1  0     0  1
#  0  1  1     1  0
#  1  0  0     1  0
#  1  0  1     0  0
#  Invariant: hi & lo == 0
#  lo = (lo ^ x) & ~hi
#  hi = ~hi & lo & x | hi & ~lo & ~x
def find_element_appears_once(A: List[int]) -> int:
    lo, hi = 0, 0
    for x in A:
        lo, hi = (lo ^ x) & ~hi, ~hi & lo & x | hi & ~lo & ~x
    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('element_appearing_once.py',
                                       'element_appearing_once.tsv',
                                       find_element_appears_once))
