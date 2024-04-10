import functools
from test_framework import generic_test


_ORDA = ord('A')
_BASE = 26


def ss_decode_col_id(col: str) -> int:
    return functools.reduce(lambda num, c: num * _BASE + ord(c) - _ORDA + 1, col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
