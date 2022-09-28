import itertools
from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    if len(service_times) <= 1: return 0
    service_times.sort()
    for i in range(1, len(service_times)):
        service_times[i] += service_times[i - 1]
    for i in range(1, len(service_times)):
        service_times[i] += service_times[i - 1]
    return service_times[-2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
