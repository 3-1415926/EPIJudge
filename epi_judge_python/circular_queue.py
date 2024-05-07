from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        self._data = [None] * max(capacity, 1)
        self._start = 0
        self._size = 0

    def _resize(self, capacity: int) -> None:
        assert capacity >= self._size * 2
        new_data = [None] * capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._start + i) % len(self._data)]
        self._data = new_data
        self._start = 0

    def enqueue(self, x: int) -> None:
        if self._size >= len(self._data):
            self._resize(len(self._data) * 2)
        self._data[(self._start + self._size) % len(self._data)] = x
        self._size += 1

    def dequeue(self) -> int:
        if self._size <= 0:
            raise ValueError()
        result = self._data[self._start]
        self._start = (self._start + 1) % len(self._data)
        self._size -= 1
        if self._size <= len(self._data) // 4:
            self._resize(max(len(self._data) // 2, 1))
        return result

    def size(self) -> int:
        return self._size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
