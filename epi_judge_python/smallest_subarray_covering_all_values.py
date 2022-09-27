import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    if len(keywords) == 0: return None
    best_subarray = None
    keyword_indices = {k: i for i, k in enumerate(keywords)}
    shortest_subarrays = {}
    for i in range(len(paragraph)):
        keyword_index = keyword_indices.get(paragraph[i])
        if keyword_index is None:
            continue
        shortest_subarray = None
        if keyword_index == 0:
            shortest_subarrays[paragraph[i]] = shortest_subarray = Subarray(i, i)
        else:
            shortest_preceding_subarray = shortest_subarrays.get(keywords[keyword_index - 1])
            if shortest_preceding_subarray:
                shortest_subarrays[paragraph[i]] = shortest_subarray = Subarray(shortest_preceding_subarray.start, i)
        if keyword_index == len(keywords) - 1 and shortest_subarray and (
            best_subarray is None or shortest_subarray.end - shortest_subarray.start < best_subarray.end - best_subarray.start):
            best_subarray = shortest_subarray
    return best_subarray


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    result = executor.run(
        functools.partial(find_smallest_sequentially_covering_subset,
                          paragraph, keywords))

    kw_idx = 0
    para_idx = result.start
    if para_idx < 0:
        raise RuntimeError('Subarray start index is negative')

    while kw_idx < len(keywords):
        if para_idx >= len(paragraph):
            raise TestFailure('Not all keywords are in the generated subarray')
        if para_idx >= len(paragraph):
            raise TestFailure('Subarray end index exceeds array size')
        if paragraph[para_idx] == keywords[kw_idx]:
            kw_idx += 1
        para_idx += 1

    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_all_values.py',
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
