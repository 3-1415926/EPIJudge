from ast import Sub
import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    if len(keywords) == 0: return Subarray(0, 0)
    best_start, best_end = 0, len(paragraph)
    cur_cover = collections.Counter()
    start = 0
    for end in range(len(paragraph)):
        if paragraph[end] in keywords:
            cur_cover[paragraph[end]] += 1
        while len(cur_cover) == len(keywords) and start <= end:
            if end - start < best_end - best_start:
                best_start, best_end = start, end            
            if paragraph[start] in cur_cover:
                cur_cover[paragraph[start]] -= 1
                if cur_cover[paragraph[start]] == 0:
                    del cur_cover[paragraph[start]]
            start += 1
    return Subarray(best_start, best_end)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
