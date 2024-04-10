import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    min_x, min_y = max(r1.x, r2.x), max(r1.y, r2.y)
    max_x, max_y = min(r1.x+r1.width, r2.x+r2.width), min(r1.y+r1.height, r2.y+r2.height)
    if max_x >= min_x and max_y >= min_y:
        return Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    return Rect(0, 0, -1, -1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
