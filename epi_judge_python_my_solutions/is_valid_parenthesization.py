from test_framework import generic_test


CLOSING = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_well_formed(s: str) -> bool:
    stack = []
    for c in s:
        opening = CLOSING.get(c)
        if opening is None:
            stack.append(c)
        else:
            if len(stack) == 0 or stack.pop() != opening: return False
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
