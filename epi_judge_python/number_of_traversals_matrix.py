from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    prev, cur = [0] * m, [1] * m
    for _ in range(1, n):
        prev, cur = cur, prev
        cur[0] = 1
        for c in range(1, m):
            cur[c] = cur[c - 1] + prev[c]
    return cur[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
