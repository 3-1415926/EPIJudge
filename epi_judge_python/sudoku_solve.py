import copy
import functools
import math
from typing import Iterable, List, Optional, Tuple

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

N = 3
NN = N * N
FULL_MASK = (1 << NN) - 1

def sqr_idx(row: int, col: int) -> int:
    return (row // N) * N + (col // N)

def num_bits(value: int) -> int:
    result = 0
    while value:
        value &= value - 1
        result += 1
    return result

def expand_mask(mask: int) -> Iterable[int]:
    for value in range(NN):
        if mask & (1 << value) != 0:
            yield value + 1    

class Solver:
    def __init__(self, partial_assignment: List[List[int]]):
        assert len(partial_assignment) == NN
        self.assignment = partial_assignment
        self.num_assigned = 0
        self.rows, self.cols, self.sqrs = ([0] * NN for _ in range(3))
        for row in range(NN):
            for col in range(NN):
                if 1 <= partial_assignment[row][col] <= NN:
                    self.mark(row, col, partial_assignment[row][col], skip_assign=True)

    def mark(self, row: int, col: int, value: int, skip_assign: bool = False):
        assert 1 <= value <= NN
        mask = 1 << (value - 1)
        self.rows[row] |= mask
        self.cols[col] |= mask
        self.sqrs[sqr_idx(row, col)] |= mask
        if not skip_assign:
            assert not self.assignment[row][col]
            self.assignment[row][col] = value
        self.num_assigned += 1

    def unmark(self, row: int, col: int):
        value = self.assignment[row][col]
        assert 1 <= value <= NN
        mask = 1 << (value - 1)
        self.rows[row] &= ~mask
        self.cols[col] &= ~mask
        self.sqrs[sqr_idx(row, col)] &= ~mask
        self.assignment[row][col] = 0
        self.num_assigned -= 1

    def find_available_cell(self) -> Tuple[int, int, int]:
        for row in range(NN):
            for col in range(NN):
                if self.assignment[row][col]:
                    continue
                taken_mask = self.rows[row] | self.cols[col] | self.sqrs[sqr_idx(row, col)]
                if taken_mask == FULL_MASK:
                    return -1, -1, 0
                return row, col, taken_mask ^ FULL_MASK
        return -1, -1, 0

    def solve(self) -> bool:
        if self.num_assigned >= NN * NN:
            return True
        row, col, free_mask = self.find_available_cell()
        if not free_mask:
            return False
        for value in expand_mask(free_mask):
            self.mark(row, col, value)
            if self.solve():
                return True
            self.unmark(row, col)
        return False


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    solver = Solver(partial_assignment)
    return solver.solve()


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
