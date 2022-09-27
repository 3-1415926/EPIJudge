import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('position', 'is_finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    endpoints = [ep for ev in A for ep in (Endpoint(ev.start, False), Endpoint(ev.finish, True))]
    endpoints.sort()
    max_count = 0
    count = 0
    for ep in endpoints:
        if not ep.is_finish:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count -= 1
    return max_count


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
