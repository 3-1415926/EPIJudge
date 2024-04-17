from test_framework import generic_test


BASE = 101
MODULO = 1 << 32


def rabin_karp(t: str, s: str) -> int:
    if len(t) < len(s):
        return -1
    t_hash, s_hash, base_factor = 0, 0, 1
    for i in range(len(s)):
        t_hash = (t_hash * BASE + ord(t[i])) % MODULO
        s_hash = (s_hash * BASE + ord(s[i])) % MODULO
        base_factor = base_factor * BASE % MODULO
    for i in range(len(s), len(t) + 1):
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)
        if i >= len(t):
            break
        t_hash = (t_hash * BASE - ord(t[i - len(s)]) * base_factor + ord(t[i])) % MODULO
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
