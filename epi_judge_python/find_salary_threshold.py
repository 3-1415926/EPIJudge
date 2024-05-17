from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    N = len(current_salaries)
    if N == 0:
        return -1
    current_salaries.sort()
    cumulative_salaries = [0] * (N + 1)
    for i in range(1, N + 1):
        cumulative_salaries[i] = cumulative_salaries[i - 1] + current_salaries[i - 1]
    left, right = 0, N
    while left < right:
        mid = (left + right) // 2
        if cumulative_salaries[mid] + (N - mid) * current_salaries[mid] < target_payroll:
            left = mid + 1
        else:
            right = mid
    return (target_payroll - cumulative_salaries[left]) / (N - left) if left < N else -1
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
