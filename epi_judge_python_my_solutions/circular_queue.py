from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int = 1) -> None:
        self._data = [None] * min(capacity, 1)
        self._left = 0
        self._right = 0
        self._count = 0
        return

    def _resize(self, target_size):
        target_size = max(target_size, 1)
        new_data = [None] * target_size
        for i in range(self._count):
            new_data[i] = self._data[(self._left + i) % len(self._data)]
        self._data = new_data
        self._left = 0
        self._right = self._count % len(self._data)

    def enqueue(self, x: int) -> None:
        if self._count == len(self._data): self._resize(self._count * 2)
        self._data[self._right] = x
        self._right = (self._right + 1) % len(self._data)
        self._count += 1

    def dequeue(self) -> int:
        if self._count == 0: raise ValueError('Dequeue from empty')
        result = self._data[self._left]
        self._data[self._left] = None
        self._left = (self._left + 1) % len(self._data)
        self._count -= 1
        if self._count <= len(self._data) // 4: self._resize(self._count)
        return result

    def size(self) -> int:
        return self._count


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
