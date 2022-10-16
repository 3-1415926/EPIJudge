import collections
import functools
import heapq
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

CharWithFrequency = collections.namedtuple('CharWithFrequency', ('c', 'freq'))
Node = collections.namedtuple('Node', ('freq', 'char', 'zero', 'one'))


def huffman_encoding(symbols: List[CharWithFrequency]) -> float:
    def average_len(node, prefix_len):
        return (node.freq * prefix_len if not node.zero and not node.one else
                average_len(node.zero, prefix_len + 1) + average_len(node.one, prefix_len + 1))

    if len(symbols) <= 1: return 0
    for i in range(len(symbols)):
        symbols[i] = Node(freq=symbols[i].freq, char=symbols[i].c, zero=None, one=None)
    heapq.heapify(symbols)
    while len(symbols) > 1:
        zero = heapq.heappop(symbols)
        one = heapq.heappop(symbols)
        heapq.heappush(symbols, Node(freq=zero.freq + one.freq, char=zero.char + one.char, zero=zero, one=one))
    return average_len(symbols[0], 0) / 100


@enable_executor_hook
def huffman_encoding_wrapper(executor, symbols):
    if any(len(x[0]) != 1 for x in symbols):
        raise RuntimeError('CharWithFrequency parser: string length is not 1')

    symbols = [CharWithFrequency(c[0], freq) for (c, freq) in symbols]
    return executor.run(functools.partial(huffman_encoding, symbols))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('huffman_coding.py',
                                       'huffman_coding.tsv',
                                       huffman_encoding_wrapper))
