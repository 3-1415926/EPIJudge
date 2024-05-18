from test_framework import generic_test


def compute_binomial_coefficient(n: int, k: int) -> int:
    k = min(k, n - k)
    result = [0] * (k + 1)
    result[0] = 1
    for i in range(1, n + 1):
        for j in reversed(range(1, min(k, n) + 1)):
            result[j] += result[j - 1]
    return result[k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
