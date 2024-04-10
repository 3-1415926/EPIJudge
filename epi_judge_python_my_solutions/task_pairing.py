import collections
from multiprocessing.sharedctypes import Value
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    if len(task_durations) % 2 == 1: raise ValueError()
    result = []
    task_durations.sort()
    for i in range(len(task_durations) // 2):
        result.append(PairedTasks(task_durations[i], task_durations[~i]))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
