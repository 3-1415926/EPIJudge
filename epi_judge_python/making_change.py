from test_framework import generic_test


COINS = [100, 50, 25, 10, 5, 1]


def change_making(cents: int) -> int:
    if cents == 0: return 0
    num_coins = 0
    for c in COINS:
        while cents >= c:
            cents -= c
            num_coins += 1
            if cents == 0: return num_coins
    raise ValueError()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
