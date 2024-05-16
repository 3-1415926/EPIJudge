from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    N = len(current_salaries)
    current_salaries.sort()
    cumulative_salaries = [0] * (N + 1)
    for i in range(1, N + 1):
        cumulative_salaries[i] = cumulative_salaries[i - 1] + current_salaries[i - 1]
    left, right = 0, N
    while left < right:
        mid = (left + right + 1) // 2
        cap = ((target_payroll - cumulative_salaries[mid]) / (N - mid)) if mid < N else float('inf')
        if cap >= current_salaries[mid - 1] if i > 0 else 0:
            left = mid
        else:
            right = mid - 1
    return (target_payroll - cumulative_salaries[left]) / (N - left) if left < N else -1.

#    20 30 40  90 100
#  0 20 50 90 180 280
#  L     M          R
#        L  M       R
#           L   M   R


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
