import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse(s: List[str], left: int, right: int):
    right -= 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: List[str]):
    reverse(s, 0, len(s))
    start_idx = None
    for i in range(len(s) + 1):
        if i < len(s) and s[i] != ' ':
            if start_idx is None:
                start_idx = i
        else:
            if start_idx is not None:
                reverse(s, start_idx, i)
                start_idx = None
                

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
