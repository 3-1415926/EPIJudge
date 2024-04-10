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


def phone_mnemonic(phone_number: str) -> List[str]:
    mnemonics = []
    indices = [0] * len(phone_number)
    while True:
        mnemonics.append(''.join(D2C[phone_number[i]][indices[i]] for i in range(len(phone_number))))
        i = len(phone_number) - 1
        while i >= 0 and indices[i] >= len(D2C[phone_number[i]]) - 1:
            i -= 1
        if i < 0:
            break
        indices[i] += 1
        i += 1
        while i < len(phone_number):
            indices[i] = 0
            i += 1
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
