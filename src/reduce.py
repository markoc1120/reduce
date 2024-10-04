"""Reduce and accumulate module"""

from typing import Callable, TypeVar

A = TypeVar("A")
B = TypeVar("B")


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    """
    assert len(x) >= 2
    ans = x[0]
    for element in x[1:]:
        ans = f(ans, element)
    return ans


def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    """
    ans = [x[0]]
    for element in x[1:]:
        ans.append(f(ans[-1], element))
    return ans


print(reduce(lambda x, y: x + y, [1, 2, 3]))
