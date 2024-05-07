from collections import deque
from dataclasses import dataclass

from test_framework import generic_test
from test_framework.test_failure import TestFailure


@dataclass
class ValueWithCount:
    value: int
    count: int
    

class QueueWithMax:
    def __init__(self):
        self._queue = deque()
        self._maxes = deque()
    
    def enqueue(self, x: int) -> None:
        while self._maxes and self._maxes[-1].value < x:
            self._maxes.pop()
        if self._maxes and self._maxes[-1].value == x:
            self._maxes[-1].count += 1
        else:
            self._maxes.append(ValueWithCount(x, 1))
        self._queue.append(x)

    def dequeue(self) -> int:
        if not self._queue:
            raise IndexError()
        if self._queue[0] == self._maxes[0].value:
            self._maxes[0].count -= 1
            if self._maxes[0].count == 0:
                self._maxes.popleft()
        return self._queue.popleft()

    def max(self) -> int:
        if not self._queue:
            raise IndexError()
        return self._maxes[0].value


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
