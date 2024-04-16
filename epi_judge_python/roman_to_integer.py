from test_framework import generic_test


VALUE = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def roman_to_integer(s: str) -> int:
    result = 0
    last_value = float('inf')
    for c in s:
        v = VALUE[c]
        if v > last_value:
            result -= last_value * 2
        result += v
        last_value = v
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
