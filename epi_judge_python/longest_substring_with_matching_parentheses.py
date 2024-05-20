from test_framework import generic_test


def longest_matching_parentheses(s: str) -> int:
    last_start, last_end = best_start, best_end = 0, -1
    open_indices = []
    for i in range(len(s)):
        if s[i] == '(':
            open_indices.append(i if i > last_end + 1 else last_start)
        elif open_indices:
            last_start, last_end = open_indices.pop(), i
            if best_end - best_start < i - last_start:
                best_start, best_end = last_start, i
    return best_end - best_start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_substring_with_matching_parentheses.py',
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
