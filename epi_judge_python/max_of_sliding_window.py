import collections
from dataclasses import dataclass
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

@dataclass
class TrafficElement:
    time: int
    volume: float


def calculate_traffic_volumes(A: List[TrafficElement],
                              w: int) -> List[TrafficElement]:
    result = [None] * len(A)
    max_idx_queue = collections.deque()
    for i in range(len(A)):
        while max_idx_queue and A[max_idx_queue[0]].time < A[i].time - w:
            max_idx_queue.popleft()
        while max_idx_queue and A[max_idx_queue[-1]].volume <= A[i].volume:
            max_idx_queue.pop()
        max_idx_queue.append(i)
        result[i] = TrafficElement(A[i].time, A[max_idx_queue[0]].volume)
    return result


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_of_sliding_window.py',
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
