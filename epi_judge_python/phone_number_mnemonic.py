from typing import List

from test_framework import generic_test, test_utils


D2C = {
    '0': '0',
    '1': '1',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
}


def phone_mnemonic(phone_number: str, start: int = 0) -> List[str]:
    if start >= len(phone_number):
        return []
    if start == len(phone_number) - 1:
        return list(D2C[phone_number[start]])
    remainders = phone_mnemonic(phone_number, start + 1)
    return [c + remainder for c in D2C[phone_number[start]] for remainder in remainders]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
