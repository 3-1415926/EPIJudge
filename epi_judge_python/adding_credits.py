import heapq
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class ClientsCreditsInfo:
    def __init__(self):
        self.all_delta = 0
        self.data = {}
        self.heap = []
    
    def insert(self, client_id: str, c: int) -> None:
        self.data[client_id] = c - self.all_delta
        heapq.heappush(self.heap, (self.all_delta - c, client_id))

    def remove(self, client_id: str) -> bool:
        old_c = self.data.pop(client_id, None)
        return old_c is not None

    def lookup(self, client_id: str) -> int:
        c = self.data.get(client_id)
        return -1 if c is None else c + self.all_delta

    def add_all(self, C: int) -> None:
        self.all_delta += C

    def max(self) -> str:
        while self.heap:
            c, client_id = heapq.heappop(self.heap)
            old_c = self.data.get(client_id)
            if old_c is not None and old_c == -c:
                return client_id            
        if not self.heap:
            raise ValueError()


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
