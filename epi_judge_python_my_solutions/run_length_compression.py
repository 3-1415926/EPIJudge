import string
from test_framework import generic_test
from test_framework.test_failure import TestFailure


DIGITS = set(string.digits)


def decoding(s: str) -> str:
    result = []
    count = 0
    for c in s:
        if c in DIGITS:
            count = count * 10 + ord(c) - ord('0')
        else:
            result.append(c * count)
            count = 0
    return ''.join(result)


def encoding(s: str) -> str:
    result = []
    start = 0
    for i in range(len(s)):
        if s[start] != s[i + 1:i + 2]:
            result.append(str(i + 1 - start) + s[start])
            start = i + 1
    return ''.join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
