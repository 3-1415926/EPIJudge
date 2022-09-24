from test_framework import generic_test


D2C = {d: str(d) for d in range(10)} | {d: chr(ord('A') + d - 10) for d in range(10, 16)}
C2D = {c: d for d, c in D2C.items()}


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if len(num_as_string) == 0: return ''
    sign = num_as_string[0] if num_as_string[0] in ('-', '+') else ''
    num = 0
    for i in range(1 if sign else 0, len(num_as_string)):
        num = num * b1 + C2D[num_as_string[i]]
    if num == 0: return '0'
    chars = []
    while num > 0:
        chars.append(D2C[num % b2])
        num //= b2
    chars.append(sign)
    return ''.join(reversed(chars))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
