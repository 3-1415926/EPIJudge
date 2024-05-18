from functools import cache
from typing import List

from test_framework import generic_test


def sqr(x: int) -> int:
    return x * x


def minimum_messiness(words: List[str], line_length: int) -> int:
    assert all(len(w) <= line_length for w in words)
    @cache
    def messiness_recursive(num_words: int) -> int:
        if num_words <= 0:
            return 0
        min_messiness = float('inf')
        cur_line = 0
        while num_words > 0:
            if cur_line:
                cur_line += 1
            cur_line += len(words[num_words - 1])
            num_words -= 1
            if cur_line > line_length:
                break
            min_messiness = min(min_messiness, messiness_recursive(num_words) + sqr(line_length - cur_line))
        return min_messiness
    return messiness_recursive(len(words))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
