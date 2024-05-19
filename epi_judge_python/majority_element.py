from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    maj_item = None
    maj_count = 0
    for item in stream:
        if maj_item is None:
            assert maj_count == 0
            maj_item = item
            maj_count += 1
        elif maj_item == item:
            maj_count += 1
        else:
            maj_count -= 1
            if maj_count <= 0:
                maj_item = None
    return maj_item


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
