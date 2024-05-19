import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse(A: List[int], start: int, end: int):
    end -= 1
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


def rotate_array(rotate_amount: int, A: List[int]) -> None:
    rotate_amount %= len(A)
    reverse(A, 0, len(A) - rotate_amount)
    reverse(A, len(A) - rotate_amount, len(A))
    reverse(A, 0, len(A))


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
