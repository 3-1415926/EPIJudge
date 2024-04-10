from test_framework import generic_test


def add(x: int, y: int) -> int:
    if x < 0 or y < 0: raise ValueError('Non-negative only')
    sum, carry, mask = 0, 0, 1
    while x >= mask or y >= mask:
        sum |= (x & mask) ^ (y & mask) ^ carry
        carry = (((x & y) | (x & carry) | (y & carry)) & mask) << 1
        mask <<= 1
    return sum | carry
        

def multiply(x: int, y: int) -> int:
    if x < 0 or y < 0: raise ValueError('Non-negative only')
    product, mask = 0, 1
    while y >= mask:
        if y & mask != 0:
            product = add(product, x)
        mask <<= 1
        x <<= 1
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
