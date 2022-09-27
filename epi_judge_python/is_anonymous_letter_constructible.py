from collections import Counter
from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_counts = Counter(magazine_text)
    letter_counts = Counter(letter_text)
    magazine_counts.subtract(letter_counts)
    return all(v >= 0 for v in magazine_counts.values())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
