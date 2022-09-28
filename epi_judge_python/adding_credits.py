from collections import namedtuple
from test_framework import generic_test
from test_framework.test_failure import TestFailure
import traceback

ClientInfo = namedtuple('ClientInfo', ('credits', 'id'))


class ClientsCreditsInfo:
    def __init__(self):
        self._max_heap = []  # of ClientInfo
        self._clients = {}   # of id -> heap index

    def _best_idx(self, op, idx, candidate_idx):
        if not 0 <= candidate_idx < len(self._max_heap): return idx
        return idx if self._max_heap[idx] == op(self._max_heap[idx], self._max_heap[candidate_idx]) else candidate_idx

    def _swap(self, i, j):
        self._clients[self._max_heap[i].id], self._clients[self._max_heap[j].id] = j, i
        self._max_heap[i], self._max_heap[j] = self._max_heap[j], self._max_heap[i]

    def _fix_heap(self, idx):
        if not 0 <= idx < len(self._max_heap): raise ValueError('Heap index out of bounds')
        while True:
            min_idx = self._best_idx(min, idx, (idx - 1) // 2)
            if min_idx == idx: break
            self._swap(idx, min_idx)
            idx = min_idx
        while True:
            max_idx = self._best_idx(max,     idx, idx * 2 + 1)
            max_idx = self._best_idx(max, max_idx, idx * 2 + 2)
            if max_idx == idx: break
            self._swap(idx, max_idx)
            idx = max_idx

    def insert(self, client_id: str, c: int) -> None:
        index = self._clients.get(client_id)
        if index is None:
            index = len(self._max_heap)
            self._max_heap.append(ClientInfo(c, client_id))
            self._clients[client_id] = index
        else:
            self._max_heap[index] = ClientInfo(c, client_id)
        self._fix_heap(index)

    def remove(self, client_id: str) -> bool:
        index = self._clients.get(client_id)
        if index is None: return False
        self._swap(index, len(self._max_heap) - 1)
        assert self._clients[client_id] == len(self._max_heap) - 1
        del self._max_heap[-1]
        self._clients.pop(client_id)
        return True

    def lookup(self, client_id: str) -> int:
        index = self._clients.get(client_id)
        if index is None: return -1
        return self._max_heap[index].credits

    def add_all(self, C: int) -> None:
        for i in range(len(self._max_heap)):
            self._max_heap[i] = ClientInfo(self._max_heap[i].credits + C, self._max_heap[i].id)

    def max(self) -> str:
        if len(self._max_heap) == 0: raise ValueError('Empty heap')
        return self._max_heap[0].id


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == 'add_all':
            cr.add_all(i_arg)
        elif op == 'lookup':
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('adding_credits.py',
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
