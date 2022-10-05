from typing import List

from test_framework import generic_test


def justify_text(words: List[str], L: int) -> List[str]:
    lines = []
    i = 0
    while i < len(words):
        sum_len = len(words[i])
        if sum_len > L: raise ValueError()
        j = i + 1
        while j < len(words) and sum_len + len(words[j]) + (j - i - 1) < L:
            sum_len += len(words[j])
            j += 1
        line = [words[i]]
        if j - i == 1:
            line.append(' ' * (L - sum_len))
        else:
            spaces_div, spaces_mod = ((L - sum_len) // (j - i - 1), (L - sum_len) % (j - i - 1)) if j < len(words) else (1, 0)
            for k in range(i + 1, j):
                line.append(' ' * (spaces_div + (k - i <= spaces_mod)))
                line.append(words[k])
            if j >= len(words):
                line.append(' ' * (L - sum_len - (j - i - 1)))
        lines.append(''.join(line))
        i = j
    return lines


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('left_right_justify_text.py',
                                       'left_right_justify_text.tsv',
                                       justify_text))
