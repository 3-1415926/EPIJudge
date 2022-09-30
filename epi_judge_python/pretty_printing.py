import functools
from typing import List

from test_framework import generic_test


def minimum_messiness(words: List[str], line_length: int) -> int:
    @functools.cache
    def recursive_messiness(words_count: int) -> int:
        if words_count <= 0: return 0
        if len(words[words_count - 1]) > line_length: raise ValueError('Word is too long')
        min_messiness = float('inf')
        cur_len = len(words[words_count - 1])
        while words_count > 0 and cur_len <= line_length:
            min_messiness = min(min_messiness, (line_length - cur_len) * (line_length - cur_len) + recursive_messiness(words_count - 1))
            words_count -= 1
            cur_len += 1 + len(words[words_count - 1])
        return min_messiness    
    return recursive_messiness(len(words))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
