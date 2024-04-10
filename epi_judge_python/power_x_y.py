from test_framework import generic_test


def power(x: float, y: int) -> float:
    # result * x ^ y = constant
    negative_power = y < 0
    y = abs(y)
    result = 1.0
    while y > 0:
        if y & 1 != 0:
            result *= x
            y -= 1
        x *= x
        y >>= 1
    return 1 / result if negative_power else result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
