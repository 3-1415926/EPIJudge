from collections import defaultdict
from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in dictionary:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return [v for v in anagrams.values() if len(v) >= 2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
