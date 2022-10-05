from test_framework import generic_test


def longest_matching_parentheses(s: str) -> int:
    def get_max_len(range_, open_char):
        max_len = 0
        start_idx, open_count = None, 0
        for i in range_:
            if s[i] == open_char:
                if open_count == 0 and start_idx is None:
                    start_idx = i
                open_count += 1
            else:
                open_count -= 1
                if open_count == 0:
                    max_len = max(max_len, abs(i - start_idx) + 1)
                elif open_count < 0:
                    open_count = 0
                    start_idx = None
        return max_len
    return max(get_max_len(range(len(s)), '('), get_max_len(reversed(range(len(s))), ')'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_substring_with_matching_parentheses.py',
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
