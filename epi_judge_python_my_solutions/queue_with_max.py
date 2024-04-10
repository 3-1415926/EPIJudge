from collections import deque

from test_framework import generic_test
from test_framework.test_failure import TestFailure


# queue: 1 5 2 8 6 7 4 3
# m-enq: 1 5 5 8 8 8 8 8
#            2   6 7 7 7
#                    4 4
#                      3    
# m-deq: 8 8 8 8 7 7 4 3
#        7 7 7 7 4 4 3 
#        4 4 4 4 3 3
#        3 3 3 3
class QueueWithMax:
    _items = deque()
    _max = deque()

    def enqueue(self, x: int) -> None:
        self._items.append(x)
        while len(self._max) > 0 and self._max[-1] < x: self._max.pop()
        self._max.append(x)

    def dequeue(self) -> int:
        if len(self._items) == 0: raise ValueError('Empty queue')
        result = self._items.popleft()
        assert len(self._max) > 0
        if self._max[0] == result: self._max.popleft()
        return result

    def max(self) -> int:
        if len(self._items) == 0: raise ValueError('Empty queue')
        return self._max[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
