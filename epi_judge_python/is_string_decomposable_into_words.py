import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    cover = [None] * (len(domain) + 1)
    cover[0] = ""
    for i in range(1, len(domain) + 1):
        for w in dictionary:
            j = i - len(w)
            if j >= 0 and cover[j] is not None and domain[j:i] == w:
                cover[i] = w
                break
    if not cover[len(domain)]:
        return []
    result = []
    i = len(domain)
    while i >= 0 and cover[i]:
        result.append(cover[i])
        i -= len(cover[i])
    assert i == 0 and cover[i] == ""
    result.reverse()
    return result


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
