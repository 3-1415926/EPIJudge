from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n < 1:
        return ''
    result = '1'
    for _ in range(1, n):
        parts = []
        count, last_digit = 0, None
        for d in result:
            if last_digit == d:
                count += 1
            else:
                if last_digit is not None:
                    parts.extend([str(count), last_digit])
                count, last_digit = 1, d
                last_digit = d
        if last_digit is not None:
            parts.extend([str(count), last_digit])
        result = ''.join(parts)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
