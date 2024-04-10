import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    j = 0
    num_a = 0
    for i in range(size):
        assert j <= i, f'Not j {j} <= i {i}'
        if s[i] != 'b':
            if s[i] == 'a':
                num_a += 1
            s[j] = s[i]
            j += 1
    size = j
    j = size + num_a
    for i in reversed(range(size)):
        assert i <= j, f'Not i {i} <= j {j}'
        if s[i] != 'a':
            j -= 1
            s[j] = s[i]
        else:
            j -= 2
            s[j + 1] = 'd'
            s[j]     = 'd'
    assert j == 0, f'j {j} != 0 at the end'
    return size + num_a


    # TODO - you fill in here.
    return 0


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
