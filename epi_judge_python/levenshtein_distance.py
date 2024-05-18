from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    prev_result, cur_result = [0] * (len(A) + 1), list(range(len(A) + 1)) 
    for bi in range(1, len(B) + 1):
        prev_result, cur_result = cur_result, prev_result
        cur_result[0] = prev_result[0] + 1
        for ai in range(1, len(A) + 1):
            cur_result[ai] = prev_result[ai - 1] if A[ai - 1] == B[bi - 1] else min(cur_result[ai - 1], prev_result[ai], prev_result[ai - 1]) + 1
    return cur_result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
