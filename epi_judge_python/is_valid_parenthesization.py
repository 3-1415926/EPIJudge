from test_framework import generic_test

PAIRS = {
    "}": "{",
    ")": "(",
    "]": "[",
}

def is_well_formed(s: str) -> bool:
    stack = []
    for c in s:
        if opening := PAIRS.get(c):
            if not stack or stack.pop() != opening:
                return False
        else:
            stack.append(c)
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
