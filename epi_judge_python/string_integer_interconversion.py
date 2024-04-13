from test_framework import generic_test
from test_framework.test_failure import TestFailure

ORD0 = ord('0')


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    is_negative = x < 0
    x = abs(x)
    digits = []
    while x != 0:
        digits.append(chr(ORD0 + (x % 10)))
        x //= 10
    digits.reverse()
    return ('-' if is_negative else '') + (''.join(digits))


def string_to_int(s: str) -> int:
    result = 0
    for ch in s:
        if ch in ('-', '+'): continue
        result = result * 10 + ord(ch) - ORD0
    if s[0] == '-':
        result = -result
    return result


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
