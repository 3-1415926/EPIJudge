from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:    
    num_combinations = [0] * (final_score + 1)
    num_combinations[0] = 1
    for ips in individual_play_scores:
        for j in range(1, final_score + 1):
            if ips <= j:
                num_combinations[j] += num_combinations[j - ips]
    return num_combinations[final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
