import collections
import functools
import traceback
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        self.visited = False


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    def dfs(vertex: GraphVertex):
        vertex.visited = True
        for edge in vertex.edges:
            if not edge.visited:
                dfs(edge)
        top_sorted.append(vertex)
    top_sorted = []
    for vertex in graph:
        if not vertex.visited:
            dfs(vertex)
    top_sorted.reverse()
    assert len(top_sorted) == len(graph)
    max_teams = collections.defaultdict(int)
    for vertex in top_sorted:
        for edge in vertex.edges:
            max_teams[edge] = max(max_teams[edge], max_teams[vertex] + 1)
    return max(max_teams.values()) + 1


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_teams_in_photograph.py',
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))
