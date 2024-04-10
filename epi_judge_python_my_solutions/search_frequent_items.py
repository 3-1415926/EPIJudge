import collections
import itertools
from typing import Iterator, List

from test_framework import generic_test, test_utils



# 1 2 3 2 3 

# Finds the candidates which may occur > n / k times.
def search_frequent_items(k: int, stream: Iterator[str]) -> List[str]:
    stream, stream_copy = itertools.tee(stream)
    frequent = collections.Counter()
    n = 0
    for item in stream:
        frequent[item] += 1
        n += 1
        if len(frequent) < k: continue
        for key in frequent.keys():
            frequent[key] -= 1
        frequent = +frequent
    for key in frequent.keys():
        frequent[key] = 0
    for item in stream_copy:
        frequent[item] += 1
    return [item for item, cnt in frequent.items() if cnt > n / k]


def search_frequent_items_wrapper(k, stream):
    return search_frequent_items(k, iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_frequent_items.py',
                                       'search_frequent_items.tsv',
                                       search_frequent_items_wrapper,
                                       test_utils.unordered_compare))
