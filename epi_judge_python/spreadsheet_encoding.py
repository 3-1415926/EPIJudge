from test_framework import generic_test

def ss_decode_col_id(col: str) -> int:
    result = 0
    ORDA = ord('A')
    BASE = ord('Z') - ORDA + 1
    for c in col:
        result = result * BASE + ord(c) - ORDA + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
