import functools
import operator
from test_framework import generic_test

MASKS = {
    1 << i: 
    functools.reduce(operator.or_, [
        ((1 << (1 << i)) - 1) << ((1 << (i + 1)) * j)
        for j in range(1 << (5 - i))
    ])
    for i in range(6)
}

def reverse_bits(x: int) -> int:
    for k, v in MASKS.items():
        x = ((x & v) << k) | ((x & (v << k)) >> k)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
