from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    x, y = map(abs, (x, y))
    if x < y: x, y = y, x
    while y:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
