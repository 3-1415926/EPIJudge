import bisect
import itertools
import math
from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    if sum(current_salaries) < target_payroll: return -1
    current_salaries.sort()
    low, high = 0, current_salaries[-1]
    while not math.isclose(low, high):
        med = (low + high) / 2
        i = bisect.bisect_left(current_salaries, med)
        total = sum(itertools.islice(current_salaries, i)) + (len(current_salaries) - i) * med
        if total >= target_payroll:
            high = med
        else:
            low = med
    return high


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
