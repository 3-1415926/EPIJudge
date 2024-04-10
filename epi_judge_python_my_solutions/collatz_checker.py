from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    verified_odd = {1}
    for start in range(3, n + 1, 2):
        i = start
        while i not in verified_odd:
            if i % 2 == 1:
                i = i * 3 + 1
            else:
                i //= 2
        verified_odd.add(start)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
