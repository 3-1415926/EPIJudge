from collections import namedtuple
from test_framework import generic_test
from test_framework.test_failure import TestFailure


LenMax = namedtuple('LenMax', 'len, max')


class Stack:
    _data = []
    _max = []

    def empty(self) -> bool:
        return len(self._data) == 0

    def max(self) -> int:
        if self.empty(): raise ValueError()
        return self._max[-1].max

    def pop(self) -> int:
        if self.empty(): raise ValueError()
        result = self._data.pop()
        if self._max[-1].len > len(self._data):
            self._max.pop()
        return result

    def push(self, x: int) -> None:
        self._data.append(x)
        if len(self._max) == 0 or x > self._max[-1].max:
            self._max.append(LenMax(len(self._data), x))


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
