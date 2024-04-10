from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    flip_bit = x & ~(x - 1)
    if flip_bit <= 1:
        flip_bit = ~x & (x + 1)
        assert flip_bit > 1
    x ^= flip_bit | (flip_bit >> 1)
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
