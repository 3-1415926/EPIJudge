import functools
from test_framework import generic_test
from test_framework.test_failure import TestFailure

ORD0 = ord('0')

def int_to_string(x: int) -> str:
    if x == 0: return '0'
    sign = '-' if x < 0 else ''
    x = abs(x)
    chars = []
    while x > 0:
        chars.append(chr(x % 10 + ORD0))
        x //= 10
    chars.append(sign)
    return ''.join(reversed(chars))


def string_to_int(s: str) -> int:
    if len(s) == 0: return 0
    sign = -1 if s[0] == '-' else 1
    result = 0
    for i in range(1 if s[0] in ('-', '+') else 0, len(s)):
        d = ord(s[i]) - ORD0
        assert 0 <= d <= 9
        result = result * 10 + d
    return sign * result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
