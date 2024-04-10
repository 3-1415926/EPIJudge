from functools import cache
from test_framework import generic_test


def is_match(regex: str, s: str, si: int = 0) -> bool:
    @cache
    def try_match(ri: int, si: int) -> bool:
        if ri >= len(regex):
            return True
        match regex[ri]:
            case '^':
                if ri != 0: raise ValueError()
                if si > 0: return False
                return try_match(ri + 1, si)
            case '$':
                if ri != len(regex) - 1: raise ValueError()
                return si >= len(s)
            case '*':
                raise ValueError()
            case '.':
                if ri + 1 < len(regex) and regex[ri + 1] == '*':
                    for si in range(si, len(s) + 1):
                        if try_match(ri + 2, si): return True
                    return False
                else:
                    if si >= len(s): return False
                    return try_match(ri + 1, si + 1)
            case _:
                if ri + 1 < len(regex) and regex[ri + 1] == '*':
                    for si in range(si, len(s) + 1):
                        if try_match(ri + 2, si): return True
                        if si < len(s) and regex[ri] != s[si]: break
                    return False
                else:
                    if si >= len(s) or regex[ri] != s[si]: return False
                    return try_match(ri + 1, si + 1)

    for si in range(si, len(s) + 1):
        if try_match(0, si): return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('regular_expression.py',
                                       'regular_expression.tsv', is_match))
