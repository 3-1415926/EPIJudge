from typing import List

from test_framework import generic_test


BASE = 10

def multiply(num1: List[int], num2: List[int]) -> List[int]:
    if not any(num1) or not any(num2):
        return [0]
    result = [0] * (len(num1) + len(num2) - 1)
    for i in reversed(range(len(num1))):
        carry = 0
        for j in reversed(range(len(num2))):
            digit = result[i + j] + abs(num1[i] * num2[j]) + carry
            result[i + j] = digit % BASE
            carry = digit // BASE
        if carry > 0:
            if i == 0:
                result.insert(0, carry)
            else:
                result[i - 1] = carry        
    if (num1[0] < 0) ^ (num2[0] < 0):
        result[0] = -result[0]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
