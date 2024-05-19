from typing import List

from test_framework import generic_test


def justify_text(words: List[str], L: int) -> List[str]:
    if not words:
        return []
    lines = []
    cur_len = len(words[0])
    start = 0
    for end in range(1, len(words)):
        next_len = cur_len + len(words[end]) + 1
        if next_len > L:
            line_parts = [words[start]]
            min_extra_spaces = (L - cur_len) // max(end - start - 1, 1)
            extra_spaces_remainder = (L - cur_len) % max(end - start - 1, 1)
            for i in range(start + 1, end):
                line_parts.append(" " * (1 + min_extra_spaces + (i - start <= extra_spaces_remainder)))
                line_parts.append(words[i])
            if start + 1 >= end:
                line_parts.append(" " * (L - cur_len))
            lines.append("".join(line_parts))
            start = end
            cur_len = len(words[start])
        else:
            cur_len = next_len
    lines.append(" ".join(words[start:]) + " " * (L - cur_len))
    return lines


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('left_right_justify_text.py',
                                       'left_right_justify_text.tsv',
                                       justify_text))
