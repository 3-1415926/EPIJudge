import copy
import functools
import math
from typing import List, Optional, Tuple

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

N = 3
NSQR = N * N
VALUE_RANGE = list(range(1, NSQR + 1))

class SudokuGrid:
    def __init__(self, partial_assignment: Optional[List[List[int]]] = None):
        self._num_remaining = NSQR * NSQR
        self._sqr_sets = [[set(VALUE_RANGE) for _ in range(N)] for _ in range(N)]
        self._row_sets = [set(VALUE_RANGE) for _ in range(NSQR)]
        self._col_sets = [set(VALUE_RANGE) for _ in range(NSQR)]
        if not partial_assignment:
            self._grid = [[0] * NSQR for _ in range(NSQR)]
            return
        self._grid = partial_assignment
        if len(self._grid) != NSQR: raise ValueError('Wrong size grid')
        for i in range(NSQR):
            if len(self._grid[i]) != NSQR: raise ValueError('Wrong size grid')
            for j in range(NSQR):
                value = self._grid[i][j]
                if value: self._grid[i][j], self[i, j] = 0, value

    def __getitem__(self, key):
        row, col = key
        return self._grid[row][col]

    def __setitem__(self, key, value):
        row, col = key
        if not value: self._reset_cell(row, col)
        else: self._set_cell(row, col, value)

    def _set_cell(self, row: int, col: int, value: int):
        if not 0 < value <= NSQR: raise ValueError('Value out of range')
        if self._grid[row][col]: self._reset_cell(row, col)
        self._num_remaining -= 1
        self._grid[row][col] = value
        assert (value in self._sqr_sets[row // N][col // N] and 
                value in self._row_sets[row] and
                value in self._col_sets[col])
        self._sqr_sets[row // N][col // N].remove(value)
        self._row_sets[row].remove(value)
        self._col_sets[col].remove(value)

    def _reset_cell(self, row: int, col: int):
        value = self._grid[row][col]
        if not value: return
        self._num_remaining += 1
        self._grid[row][col] = 0
        assert (value not in self._sqr_sets[row // N][col // N] and 
                value not in self._row_sets[row] and
                value not in self._col_sets[col])
        self._sqr_sets[row // N][col // N].add(value)
        self._row_sets[row].add(value)
        self._col_sets[col].add(value)
        
    def _get_least_ambiguous_cell(self):
        min_row_set_len = min(len(self._row_sets[r]) for r in range(NSQR) if self._row_sets[r])
        min_rows = [r for r in range(NSQR) if len(self._row_sets[r]) == min_row_set_len]
        min_col_set_len = min(len(self._col_sets[c]) for c in range(NSQR) if self._col_sets[c])
        min_cols = [c for c in range(NSQR) if len(self._col_sets[c]) == min_col_set_len]
        for min_row in min_rows:
            for min_col in min_cols:
                if not self._grid[min_row][min_col]:
                    return min_row, min_col
        min_sqr_set_len = min(len(self._sqr_sets[r][c]) for r in range(N) for c in range(N) if self._sqr_sets[r][c])
        min_sqr_starts = [(r * N, c * N) for r in range(N) for c in range(N) if len(self._sqr_sets[r][c]) == min_sqr_set_len]
        for min_sqr_row_start, min_sqr_col_start in min_sqr_starts:
            for min_row in min_rows:
                if min_sqr_row_start <= min_row < min_sqr_row_start + N:
                    for i in range(N):
                        if not self._grid[min_row][min_sqr_col_start + i]:
                            return min_row, min_sqr_col_start + i
            for min_col in min_cols:
                if min_sqr_col_start <= min_col < min_sqr_col_start + N:
                    for i in range(N):
                        if not self._grid[min_sqr_row_start + i][min_col]:
                            return min_sqr_row_start + i, min_col
        min_set_len = min(min_row_set_len, min_col_set_len, min_sqr_set_len)
        if min_row_set_len == min_set_len:
            for c in range(NSQR):
                if not self._grid[min_rows[0]][c]: return min_rows[0], c
        elif min_col_set_len == min_set_len:
            for r in range(NSQR):
                if not self._grid[r][min_cols[0]]: return r, min_cols[0]
        else:
            for r in range(min_sqr_starts[0][0], min_sqr_starts[0][0] + N):
                for c in range(min_sqr_starts[0][1], min_sqr_starts[0][1] + N):
                    if not self._grid[r][c]: return r, c
        assert False

    def __repr__(self):
        return '\n'.join(' '.join(str(self[r, c]) for c in range(NSQR)) for r in range(NSQR))

    def solve(self):
        if self._num_remaining <= 0: return True
        row, col = self._get_least_ambiguous_cell()
        for v in self._row_sets[row] & self._col_sets[col] & self._sqr_sets[row // N][col // N]:
            self._set_cell(row, col, v)
            if self.solve(): return True
            self._reset_cell(row, col)
        return False            




def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    sudoku = SudokuGrid(partial_assignment)
    return sudoku.solve()


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
