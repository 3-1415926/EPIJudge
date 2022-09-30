import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    last_len = [0] + [None] * (len(domain))
    dict_lengths = sorted(set(map(len, dictionary)))
    for i in range(len(domain)):
        if last_len[i] is None: continue
        for dl in dict_lengths:
            if i + dl > len(domain): break
            subword = domain[i:i+dl]
            if subword in dictionary:
                last_len[i + dl] = dl
    if last_len[-1] is None: return []
    result = []
    i = len(domain)
    while i > 0:
        result.append(domain[i - last_len[i]:i])
        i -= last_len[i]
    for i in range(len(result) // 2):
        result[i], result[~i] = result[~i], result[i]
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
