import math
from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    sieve = [i >= 2 for i in range(n + 1)]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if not sieve[i]: continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
