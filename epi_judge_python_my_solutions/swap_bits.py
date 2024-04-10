from test_framework import generic_test


def swap_bits(x, i, j):
    if (x & (1 << i)) >> i != (x & (1 << j)) >> j:
        x ^= (1 << i) | (1 << j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
