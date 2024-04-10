from test_framework import generic_test

NUM_BITS = 64

def parity(x: int) -> int:
    assert x >= 0 and x < (1 << (NUM_BITS - 1))
    shift = NUM_BITS 
    while shift > 1:
        shift >>= 1
        x ^= x >> shift
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
