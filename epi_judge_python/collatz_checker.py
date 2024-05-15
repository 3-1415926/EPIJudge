from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    assert n >= 1
    already_true = set()
    for i in range(3, n + 1, 2):
        current_sequence = set()
        j = i
        while j >= i and j not in already_true:
            current_sequence.add(j)
            if j % 2 == 0:
                j //= 2
            else:
                j = 3 * j + 1
        already_true.update(current_sequence)
        already_true.discard(i)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
