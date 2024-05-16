import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    endpoints = [e for a in A for e in (Endpoint(a.start, False), Endpoint(a.finish, True))]
    endpoints.sort()
    max_simultaneous = 0
    num_simultaneous = 0
    for e in endpoints:
        if e.is_finish:
            num_simultaneous -= 1
        else:
            num_simultaneous += 1
            if max_simultaneous < num_simultaneous:
                max_simultaneous = num_simultaneous
    return max_simultaneous


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
