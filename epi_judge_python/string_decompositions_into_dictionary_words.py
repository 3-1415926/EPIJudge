from collections import Counter
import heapq
from typing import List

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    if len(words) == 0: return []
    word_len = len(words[0])
    results = [[] for _ in range(word_len)]
    assert all(len(w) == word_len for w in words)
    initial_counts = Counter(words)
    for shift in range(word_len):
        cur_counts = Counter()
        start_idx = shift
        for i in range(shift, len(s), word_len):
            word = s[i:i + word_len]
            if initial_counts[word] == 0:
                cur_counts.clear()
                start_idx = i + word_len
                continue
            while initial_counts[word] - cur_counts[word] <= 0:
                cur_counts[s[start_idx:start_idx + word_len]] -= 1
                start_idx += word_len                
            cur_counts[word] += 1
            if cur_counts.total() == len(words):
                results[shift].append(start_idx)
                cur_counts[s[start_idx:start_idx + word_len]] -= 1
                start_idx += word_len                       
    return list(heapq.merge(*results))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
