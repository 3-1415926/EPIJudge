import collections
import math
from typing import List

from test_framework import generic_test


SQRT2 = math.sqrt(2)

class HeapEntry(collections.namedtuple('HeapEntry', ['value', 'a', 'b'])):
    @staticmethod
    def make(a, b):
        return HeapEntry(a + b * SQRT2, a, b)


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    if k == 0: return []
    result = [HeapEntry.make(0, 0)]
    i, j = 0, 0
    for k in range(1, k):
        next_i_entry = HeapEntry.make(result[i].a + 1, result[i].b)
        next_j_entry = HeapEntry.make(result[j].a, result[j].b + 1)
        if next_i_entry < next_j_entry:
            result.append(next_i_entry)
            i += 1
        elif next_i_entry > next_j_entry:
            result.append(next_j_entry)
            j += 1            
        else:
            result.append(next_i_entry)
            i += 1
            j += 1
    return [r.value for r in result]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
