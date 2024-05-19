from test_framework import generic_test


COINS = [100, 50, 25, 10, 5, 1]


def change_making(cents: int) -> int:
    num_coins = 0
    ci = 0
    while cents:
        if cents >= COINS[ci]:
            cents -= COINS[ci]
            num_coins += 1
        else:
            ci += 1
    return num_coins


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('making_change.py', 'making_change.tsv',
                                       change_making))
