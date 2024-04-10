from test_framework import generic_test


def parity(x: int) -> int:
    if x < 0: raise ValueError('Non-negative only')
    shift = 1
    while x >= (1 << shift):
        shift *= 2
    while shift > 1:
        shift //= 2
        x ^= x >> shift
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
