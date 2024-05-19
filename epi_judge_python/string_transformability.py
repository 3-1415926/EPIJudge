from collections import deque
from typing import Set

from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    queue = deque([(s, 0)])
    D.remove(s)
    while queue:
        word, dist = queue.popleft()
        if word == t:
            return dist
        for k in range(len(word)):
            for c in range(ord('a'), ord('z') + 1):
                d = word[:k] + chr(c) + word[k+1:]
                if d in D:
                    D.remove(d)
                    queue.append((d, dist + 1))
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
