from collections import deque
from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    steps = deque([1], maxlen=maximum_step + 1)
    for i in range(1, top + 1):
        last_steps = 0
        for j in range(1, min(maximum_step, i) + 1):
            if i - j >= 0:
                last_steps += steps[-j]
        steps.append(last_steps)
    return steps[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
