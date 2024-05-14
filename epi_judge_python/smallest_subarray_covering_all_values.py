import functools
from typing import List, NamedTuple

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

class Subarray(NamedTuple):
    start: int
    end: int

    @property
    def length(self):
        return self.end - self.start if 0 <= self.start <= self.end else float('inf')


def find_smallest_sequentially_covering_subset(paragraph: List[str],
                                               keywords: List[str]
                                               ) -> Subarray:
    best_subarray = Subarray(-1, -1)
    subsubarrays = [None] * len(keywords)
    kw_indices = {k: i for i, k in enumerate(keywords)}
    for i in range(len(paragraph)):
        kw_idx = kw_indices.get(paragraph[i])
        if kw_idx is None:
            continue
        if kw_idx == 0:
            subsubarrays[kw_idx] = Subarray(i, i)
        elif subsubarrays[kw_idx - 1] is not None:
            subsubarrays[kw_idx] = Subarray(subsubarrays[kw_idx - 1].start, i)
        if kw_idx == len(keywords) - 1 and subsubarrays[kw_idx] is not None and best_subarray.length > subsubarrays[kw_idx].length:
            best_subarray = subsubarrays[kw_idx]
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
