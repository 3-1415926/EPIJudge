from test_framework import generic_test


ORD0 = ord('0')
ORDA = ord('A')
BASE_THRESHOLD = 10

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    number = 0
    for ch in num_as_string.upper():
        if ch in ('-', '+'):
            continue
        ord_ch = ord(ch)
        number = number * b1 + ord_ch - (ORD0 if ord_ch < ORD0 + BASE_THRESHOLD else ORDA - BASE_THRESHOLD)
    if number == 0:
        return '0'
    digits = []
    while number != 0:
        digit = number % b2
        digits.append(chr(digit + (ORD0 if digit < BASE_THRESHOLD else ORDA - BASE_THRESHOLD)))
        number //= b2
    digits.reverse()
    return ('-' if num_as_string[0] == '-' else '') + (''.join(digits))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
