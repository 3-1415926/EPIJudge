import functools
from itertools import cycle
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def rotate_array(rotate_amount: int, A: List[int]) -> None:
    num_cycles = gcd(len(A), rotate_amount)
    cycle_len = len(A) // num_cycles
    for c in range(num_cycles):
        temp = A[c]
        for i in range(cycle_len):
            j = (c + rotate_amount * i) % len(A)
            A[j], temp = temp, A[j]
        A[c] = temp


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
