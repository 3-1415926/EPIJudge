from test_framework import generic_test


def longest_matching_parentheses_with_stack(s: str) -> int:
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


def longest_matching_parentheses(s: str) -> int:
    def longest_matching_one_way(r: range, open_char: str) -> int:
        longest = 0
        nest_level, start = 0, r.start
        for i in r:
            if s[i] == open_char:
                nest_level += 1
            elif nest_level == 0:
                start = i + r.step
            else:
                nest_level -= 1
                if nest_level == 0:
                    longest = max(longest, abs(i - start) + 1)
        return longest
    return max(longest_matching_one_way(range(len(s)), '('),
               longest_matching_one_way(range(len(s)-1, -1, -1), ')'))
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_substring_with_matching_parentheses.py',
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
