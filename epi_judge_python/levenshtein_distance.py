from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    if len(A) < len(B): A, B = B, A
    prev_ld = [None] * (len(B) + 1)
    ld = list(range(len(B) + 1))
    for i in range(1, len(A) + 1):
        prev_ld, ld = ld, prev_ld
        ld[0] = i
        for j in range(1, len(B) + 1):
            ld[j] = min(prev_ld[j - 1] + (A[i - 1] != B[j - 1]), ld[j - 1] + 1, prev_ld[j] + 1)
    return ld[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
