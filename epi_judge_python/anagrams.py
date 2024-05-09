import collections
from typing import List

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    groups = collections.defaultdict(list)
    for item in dictionary:
        groups[''.join(sorted(item))].append(item)
    return [g for g in groups.values() if len(g) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
