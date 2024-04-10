from test_framework import generic_test


def count_bits(x: int) -> int:
    if x < 0: raise ValueError('Only non-negative')
    cnt = 0
    while x > 0:
        x &= x - 1
        cnt += 1
    return cnt



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
