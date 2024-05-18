from test_framework import generic_test


def fibonacci(n: int) -> int:
    prev, cur = 1, 0
    for i in range(n):
        prev, cur = cur, prev + cur    
    return cur


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
