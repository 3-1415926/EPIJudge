from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    x, y = abs(x), abs(y)
    if x < y: x, y = y, x
    shift = 0
    while x > 0 and y > 0 and x != y:
        if (x & 1) == 0:
            if (y & 1) == 0:
                shift += 1
                x >>= 1
                y >>= 1
            else:
                x >>= 1
        else:
            if (y & 1) == 0:
                y >>= 1
            elif x > y:
                x -= y
            else:
                y -= x            
    return max(x, y) << shift


if __name__ == '__main__':
    exit(generic_test.generic_test_main('gcd.py', 'gcd.tsv', gcd))
