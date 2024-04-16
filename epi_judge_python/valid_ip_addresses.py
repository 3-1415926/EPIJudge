from functools import cache
from typing import Iterable, List

from test_framework import generic_test


@cache
def get_valid_ip_address(s: str, start_idx: int = 0, num_remaining: int = 4) -> List[str]:
    results = []
    part_value = 0
    for i in range(start_idx, min(len(s), start_idx + 3)):
        part_value = part_value * 10 + ord(s[i]) - ord('0')
        if part_value > 255:
            break
        part = s[start_idx:i+1]
        if num_remaining > 1:
            for subaddress in get_valid_ip_address(s, i + 1, num_remaining - 1):
                results.append(part + "." + subaddress)
        elif i == len(s) - 1:
            results.append(part)
        if s[start_idx] == '0':
            break
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
