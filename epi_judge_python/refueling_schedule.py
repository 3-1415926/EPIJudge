import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    if len(gallons) != len(distances): raise ValueError()
    prev_tank, prev_distance = 0, 0
    tank = [None] * len(gallons)
    for i in range(len(gallons)):
        tank[i] = prev_tank - prev_distance / MPG
        prev_tank = tank[i] + gallons[i]
        prev_distance = distances[i]
    assert prev_tank - prev_distance / MPG == 0
    return min(range(len(gallons)), key=lambda i: tank[i])


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
