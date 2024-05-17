from typing import List

from test_framework import generic_test


def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    N = len(current_salaries)
    if N == 0:
        return -1.
    current_salaries.sort()
    cumulative_salaries = current_salaries.copy()
    for i in range(1, N):
        cumulative_salaries[i] += cumulative_salaries[i - 1]
    left, right = 0, N
    while left < right:
        mid = (left + right + 1) // 2
        cap = (target_payroll - cumulative_salaries[mid - 1]) / (N - left) if left < N else float('inf')
        print(left, mid, right, cap)
        if cap >= current_salaries[mid - 1]:
            left = mid
        else:
            right = mid - 1
    print(left, right)         
    if left == N:
        return current_salaries[-1] if cumulative_salaries[-1] == target_payroll else -1.
    if left == 0:
        return target_payroll / N
    return (target_payroll - cumulative_salaries[left - 1]) / (N - left)
        

# 20 30 40 90 100
#  0 20 50 90 180 280
#  L        M       R  
#        L  M       R
#           L   M   R


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
