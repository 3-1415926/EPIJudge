import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    _counter = 0
    def __init__(self) -> None:
        self.id = GraphVertex._counter = GraphVertex._counter + 1
        self.d = None
        self.edges: List[GraphVertex] = []
    def __repr__(self):
        edges_str = ', '.join(str(e.id) for e in self.edges)
        return f'{self.id} ({self.d}) -> [{edges_str}]'


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def dfs(vertex: GraphVertex, is_left: bool):
        vertex.d = is_left
        for edge in vertex.edges:
            if edge.d is None:
                if not dfs(edge, not is_left): return False
            else:
                if edge.d == is_left: return False
        return True
    return all(dfs(v, True) for v in graph if v.d is None)

def is_any_placement_feasible_via_bfs(graph: List[GraphVertex]) -> bool:
    def bfs(vertex: GraphVertex):
        queue = collections.deque([vertex])
        vertex.d = 0
        while queue:
            vertex = queue.popleft()
            for edge in vertex.edges:
                if edge.d is None:
                    edge.d = vertex.d + 1
                    queue.append(edge)
                elif edge.d % 2 == vertex.d % 2:
                    return False
        return True
    return all(bfs(v) for v in graph if v.d is None)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
