import operator
from test_framework import generic_test


DELIMITER = ','
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def evaluate(expression: str) -> int:
    stack = []
    parts = expression.split(DELIMITER)
    for p in parts:
        op = OPERATORS.get(p)
        if op is None:
            stack.append(int(p))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(op(a, b))
    assert len(stack) == 1
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
