import collections
from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    deque = collections.deque([0] * (maximum_step - 1) + [1], maxlen=maximum_step)
    for _ in range(top):
        deque.append(sum(deque))
    return deque[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
