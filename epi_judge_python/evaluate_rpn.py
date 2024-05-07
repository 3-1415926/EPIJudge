from test_framework import generic_test


DELIM = ','
OPERATORS = {
    '*': int.__mul__,
    '/': int.__floordiv__,
    '+': int.__add__,
    '-': int.__sub__,
}


def evaluate(expression: str) -> int:
    stack = []
    for token in expression.split(DELIM):
        if oper := OPERATORS.get(token, None):
            b, a = stack.pop(), stack.pop()
            stack.append(oper(a, b))
        else:
            stack.append(int(token))
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
