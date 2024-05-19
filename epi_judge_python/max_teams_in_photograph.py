import collections
import functools
from typing import List, Optional

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


UNVISITED, PROCESSING, VISITED = range(3)


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = UNVISITED to indicate unvisitied vertex.
        self.max_distance = UNVISITED


def top_sort(graph: List[GraphVertex]) -> Optional[List[GraphVertex]]:
    top_sorted = []
    def dfs(vertex: GraphVertex) -> bool:
        if vertex.max_distance == VISITED:
            return True
        if vertex.max_distance == PROCESSING:
            return False
        vertex.max_distance = PROCESSING
        for edge in vertex.edges:
            dfs(edge)
        vertex.max_distance = VISITED
        top_sorted.append(vertex)
        return True
    for vertex in graph:
        if not dfs(vertex):
            return None
    top_sorted.reverse()
    return top_sorted


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    graph = top_sort(graph)
    if graph is None:
        return 0
    longest_path = collections.defaultdict(int)
    for vertex in graph:
        for edge in vertex.edges:
            longest_path[edge] = max(longest_path[edge], longest_path[vertex] + 1)
    return max(longest_path.values()) + 1


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
