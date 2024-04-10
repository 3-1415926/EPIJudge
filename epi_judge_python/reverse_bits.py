from test_framework import generic_test


NUM_BITS = 64

def reverse_bits(x: int) -> int:
    assert x >= 0 and x < (1 << 63)
    mask_width = NUM_BITS >> 1
    mask = (1 << mask_width) - 1
    while mask_width > 0:
        x = ((x >> mask_width) & mask) | ((x & mask) << mask_width)
        mask_width >>= 1
        mask ^= mask << mask_width
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
