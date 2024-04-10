import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

Interval = collections.namedtuple('Interval', ('start', 'length'))

def intersect_interval(i1: Interval, i2: Interval) -> Interval:
    if i1.start + i1.length < i2.start or i2.start + i2.length < i1.start:
        return None
    start = max(i1.start, i2.start)
    end = min(i1.start + i1.length, i2.start + i2.length)
    return Interval(start, end - start)


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if (x_interval := intersect_interval(Interval(r1.x, r1.width), Interval(r2.x, r2.width))) is None:
        return Rect(0, 0, -1, -1)
    if (y_interval := intersect_interval(Interval(r1.y, r1.height), Interval(r2.y, r2.height))) is None:
        return Rect(0, 0, -1, -1)
    return Rect(x_interval.start, y_interval.start, x_interval.length, y_interval.length)


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
