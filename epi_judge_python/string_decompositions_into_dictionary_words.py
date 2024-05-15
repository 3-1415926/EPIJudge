import collections
import heapq
from typing import List

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    if not words:
        return []
    results = []
    word_len = len(words[0])
    assert all(len(w) == word_len for w in words)
    for offset in range(word_len):
        uncovered = collections.Counter(words)
        num_uncovered = len(uncovered)
        results.append([])
        get_idx = lambda pos: pos * word_len + offset
        for end in range(1, (len(s) - offset) // word_len + 1):
            start = end - len(words)
            if start > 0:
                start_word = s[get_idx(start - 1):get_idx(start)]
                if start_word in uncovered:
                    num_uncovered += uncovered[start_word] == 0
                    uncovered[start_word] += 1
            end_word = s[get_idx(end - 1):get_idx(end)]
            if end_word in uncovered:
                uncovered[end_word] -= 1
                num_uncovered -= uncovered[end_word] == 0
            if num_uncovered == 0:
                results[-1].append(get_idx(start))
    return list(heapq.merge(*results))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
