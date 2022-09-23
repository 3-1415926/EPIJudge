from sre_constants import CATEGORY_WORD
from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if len(num1) == 0 or len(num2) == 0: return [0]
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0] = abs(num1[0])
    num2[0] = abs(num2[0])
    product = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        carry = 0
        for j in range(len(num2)):
            product[i + j] += num1[~i] * num2[~j] + carry
            carry, product[i + j] = product[i + j] // 10, product[i + j] % 10
        if carry > 0:
            product[i + len(num2)] += carry
            assert product[i + len(num2)] <= 10
    while product[-1] == 0 and len(product) > 1:
        del product[-1]
    for i in range(len(product) // 2):
        product[i], product[len(product) - i - 1] = product[len(product) - i - 1], product[i]
    product[0] *= sign
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
