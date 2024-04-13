import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    final_size = 0
    j = 0
    for i in range(size):
        if s[i] != 'b':
            final_size += 2 if s[i] == 'a' else 1
            s[j] = s[i]
            j += 1
    size = j
    j = final_size
    for i in reversed(range(size)):
        if s[i] == 'a':
            j -= 2
            s[j:j+2] = 'dd'
        else:
            j -= 1
            s[j] = s[i]
    del s[final_size:]
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
