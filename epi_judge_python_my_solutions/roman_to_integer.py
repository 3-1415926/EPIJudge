from test_framework import generic_test


R2D = {
    '': 0,
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_integer(s: str) -> int:
    num = 0
    for i in range(len(s)):
        num += R2D[s[i]] * (1 if R2D[s[i]] >= R2D[s[i+1:i+2]] else -1)
    return num


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
