from multiprocessing.sharedctypes import Value
from test_framework import generic_test

# n\k 0 1 2 3 4 5
# 0 : 1 0 0 0 0 0
# 1 : 1 1 0 0 0 0
# 2 : 1 2 1 0 0 0
# 3 : 1 3 3 1 0 0
# 4 : 1 4 6 4 1 0
# 5 : 1 51010 5 1
def compute_binomial_coefficient(n: int, k: int) -> int:
    if n < 0 or k < 0: raise ValueError()
    if k > n: return 0
    if k > n // 2: k = n - k
    coef = [1] + [0] * k
    for i in range(1, n + 1):
        for j in range(min(k, i), 0, -1):
            coef[j] += coef[j - 1]
    return coef[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
