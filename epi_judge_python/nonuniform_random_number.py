from asyncio import proactor_events
import collections
import functools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook


def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:
    if len(values) != len(probabilities): raise ValueError()
    if len(values) == 0: raise ValueError()
    # probabilities = list(itertools.accumulate(probabilities))
    for i in range(1, len(values)):
        probabilities[i] += probabilities[i - 1]
    key = random.random()
    # l = bisect.bisect_left(probabilities, key)
    l, r = 0, len(probabilities)
    while l < r:
        m = (l + r) // 2
        if key <= probabilities[m]:
            r = m
        else:
            l = m + 1
    assert l == r
    return values[l]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
