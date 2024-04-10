from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y < 0:
        if x == 0: return float('NaN')
        x = 1 / x
        y = -y
    # Invariant: result * x ** y
    result = 1
    while y > 0:
        if y % 2 != 0:
            result *= x
            y -= 1
        else:
            x *= x
            y //= 2
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
