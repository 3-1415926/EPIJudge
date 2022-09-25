from typing import List

from test_framework import generic_test


NUM_PARTS = 4
MAX_PART = 255
MAX_PART_LEN = len(str(MAX_PART))



def valid_ip_addresses(s, start, num_parts):
    if start >= len(s) or num_parts <= 0:
        if start == len(s) and num_parts == 0:
            yield ''
        return
    for end in range(start + MAX_PART_LEN if s[start] != '0' else start + 1, start, -1):
        if int(s[start:end]) <= MAX_PART:
            for ip in valid_ip_addresses(s, end, num_parts - 1):
                yield s[start:end] + ('.' + ip if ip else '')


def get_valid_ip_address(s: str) -> List[str]:
    return list(valid_ip_addresses(s, 0, NUM_PARTS))


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
