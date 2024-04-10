from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    mask = 0b11
    while x & mask in (0, mask):
        mask <<= 1
    return x ^ mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
