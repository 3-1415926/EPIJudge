from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    parts = []
    current_run = 0
    for c in s:
        if c < '0' or '9' < c:
            parts.append(c * current_run)
            current_run = 0
        else:
            current_run = current_run * 10 + ord(c) - ord('0')
    return ''.join(parts)


def encoding(s: str) -> str:
    parts = []
    current_run = 0
    for i in range(len(s)):
        current_run += 1
        if i >= len(s) - 1 or s[i] != s[i + 1]:
            parts.append(str(current_run))
            parts.append(s[i])
            current_run = 0
    return ''.join(parts)


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
