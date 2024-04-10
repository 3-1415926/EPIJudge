from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    cur_majority = None
    cur_count = 0
    for item in stream:
        if cur_count == 0 or cur_majority == item:
            cur_majority = item
            cur_count += 1
        else:
            cur_count -= 1
    return cur_majority


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
