import collections
from typing import Set

from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    def word_patterns(word):
        for k in range(word_len):
            yield word[:k] + '?' + word[k+1:]

    word_len = len(s)
    assert s in D and t in D
    assert all(len(d) == word_len for d in D)
    p2d = collections.defaultdict(set)
    for w in D:
        for p in word_patterns(w):
            p2d[p].add(w)
    
    queue = collections.deque([(s, 0)])
    while queue:
        w, dist = queue.popleft()
        if w not in D: continue
        D.remove(w)
        for p in word_patterns(w):
            for e in p2d[p]:
                if e == t: return dist + 1
                if e in D: queue.append((e, dist + 1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
