from functools import reduce
from test_framework import generic_test


class HashUpdater:
    def __init__(self, s, hash_length, hash_factor=1000000007, hash_mod=1 << 32):
        self._hash = 0
        self._s = s
        self._length = hash_length
        self._mod = hash_mod
        self._factor = hash_factor
        self._factor_last = reduce(lambda a, _: a * self._factor % self._mod,
                                   range(self._length - 1), 1)

    def push(self, c):
        self._hash = (self._hash * self._factor + ord(c)) % self._mod

    def pop(self, c):
        self._hash = (self._hash - ord(c) * self._factor_last) % self._mod

    def __hash__(self):
        return self._hash

    def __eq__(self, other):        
        return type(self) is type(other) and self._hash == other._hash
    
    def __str__(self):
        return str(self._hash)
        

def are_equal(t, s, i):
    for j in range(len(s)):
        if t[i + j] != s[j]:
            return False
    return True



def rabin_karp(t: str, s: str) -> int:
    if len(t) < len(s): return -1
    t_hash = HashUpdater(t, len(s))
    s_hash = HashUpdater(s, len(s))
    for i in range(len(s)):
        t_hash.push(t[i])
        s_hash.push(s[i])
    for i in range(0, len(t) - len(s) + 1):
        if t_hash == s_hash and are_equal(t, s, i):
            return i
        t_hash.pop(t[i])
        if i < len(t) - len(s):
            t_hash.push(t[i + len(s)])
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
