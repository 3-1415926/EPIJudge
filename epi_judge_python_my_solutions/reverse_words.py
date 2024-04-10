import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def reverse(items, start=0, end=None):
    if end is None: end = len(items)
    for i in range((end - start) // 2):
        items[start + i], items[end - i - 1] = items[end - i - 1], items[start + i]


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    start = None
    for i in range(len(s)):
        if s[i] != ' ':
            if start is None: start = i
        else:
            if start is not None:
                reverse(s, start, i)
                start = None
    if start is not None:
        reverse(s, start, len(s))
        start = None
    reverse(s)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
