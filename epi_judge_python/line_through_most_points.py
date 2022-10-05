import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class Point(collections.namedtuple('Point', ('x', 'y'))):
    def __repr__(self):
        return f'({self.x}, {self.y})'

class Line(collections.namedtuple('Line', ('kx', 'ky', 't'))):
    def __repr__(self):
        return f'{self.kx}x {"+" if self.ky >= 0 else "-"} {abs(self.ky)}y = {self.t}'

def gcd(a: int, b: int, c: int = None):
    a = abs(a)
    b = abs(b)
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a if c is None else gcd(a, c)

# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)
# (x - x1) * (y2 - y1) = (y - y1) * (x2 - x1)
# x * (y2 - y1) + y * (x1 - x2) = x1 * (y2 - y1) + y1 * (x1 - x2)
def find_line(a: Point, b: Point) -> Line:
    kx = b.y - a.y
    ky = a.x - b.x
    t = a.x * kx + a.y * ky
    divisor = gcd(kx, ky, t)
    if kx < 0: kx, ky, t = -kx, -ky, -t
    elif kx == 0:
        if ky < 0: ky, t = -ky, -t
        elif ky == 0: t = -t
    return Line(kx // divisor, ky // divisor, t // divisor)

def find_line_with_most_points(points: List[Point]) -> int:
    max_points = 0
    for i in range(len(points)):
        if max_points >= len(points) - i: break
        line_points = collections.defaultdict(int)  
        overlap_points = 1
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                overlap_points += 1
                continue
            line = find_line(points[i], points[j])
            line_points[line] += 1
        max_points = max(max_points, max(line_points.values(), default=0) + overlap_points)
    return max_points

@enable_executor_hook
def find_line_with_most_points_wrapper(executor, points):
    points = [Point(*x) for x in points]
    return executor.run(functools.partial(find_line_with_most_points, points))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('line_through_most_points.py',
                                       'line_through_most_points.tsv',
                                       find_line_with_most_points_wrapper))
