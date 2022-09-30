from test_framework import generic_test

def number_of_ways(n: int, m: int) -> int:
    if n < m: n, m = m, n
    if n <= 0 or m <= 0: return 0
    cur = [1] * m
    for _ in range(1, n):
        for j in range(1, m):
            cur[j] += cur[j - 1]
    return cur[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
