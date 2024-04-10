import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Person = collections.namedtuple('Person', ('age', 'name'))


def group_by_age(people: List[Person]) -> None:
    rights = collections.Counter()
    for p in people:
        rights[p.age] += 1
    accum = 0
    for age in rights.keys():
        accum += rights[age]
        rights[age] = accum
    assert accum == len(people)
    lefts = rights.copy()
    i = 0
    while i < len(people):
        if lefts[people[i].age] <= i < rights[people[i].age]:
            i += 1
        else:
            lefts[people[i].age] -= 1
            people[lefts[people[i].age]], people[i] = people[i], people[lefts[people[i].age]]
    


@enable_executor_hook
def group_by_age_wrapper(executor, people):
    if not people:
        return
    people = [Person(*x) for x in people]
    values = collections.Counter()
    values.update(people)

    executor.run(functools.partial(group_by_age, people))

    if not people:
        raise TestFailure('Empty result')

    new_values = collections.Counter()
    new_values.update(people)
    if new_values != values:
        raise TestFailure('Entry set changed')

    ages = set()
    last_age = people[0].age

    for x in people:
        if x.age in ages:
            raise TestFailure('Entries are not grouped by age')
        if last_age != x.age:
            ages.add(last_age)
            last_age = x.age


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('group_equal_entries.py',
                                       'group_equal_entries.tsv',
                                       group_by_age_wrapper))
