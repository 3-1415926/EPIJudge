from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    _enqueue_stack = []
    _dequeue_stack = []

    def enqueue(self, x: int) -> None:
        self._enqueue_stack.append(x)

    def dequeue(self) -> int:
        if len(self._dequeue_stack) == 0:
            while len(self._enqueue_stack) > 0:
                self._dequeue_stack.append(self._enqueue_stack.pop())
        if len(self._dequeue_stack) == 0:
            raise ValueError('Empty queue')
        return self._dequeue_stack.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
