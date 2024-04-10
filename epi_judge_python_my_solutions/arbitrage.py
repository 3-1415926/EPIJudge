import math
from typing import List

from test_framework import generic_test


def is_arbitrage_exist(graph: List[List[float]]) -> bool:
    N = len(graph)
    for i in range(N):
        for j in range(N):
            graph[i][j] = -math.log(graph[i][j])
    min_len = [float('inf')] * N
    min_len[0] = 0
    for _ in range(N - 1):
        for i in range(N):
            for j in range(N):
                if min_len[j] > min_len[i] + graph[i][j]:
                    min_len[j] = min_len[i] + graph[i][j]
    for i in range(N):
        for j in range(N):
            if min_len[j] > min_len[i] + graph[i][j]:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('arbitrage.py', 'arbitrage.tsv',
                                       is_arbitrage_exist))
