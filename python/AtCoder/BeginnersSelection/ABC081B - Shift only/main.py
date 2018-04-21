# -*- coding: utf-8 -*-
N = int(input())
numbers = map(int, input().split())


def calcMaxShiftableTimes(n: int) -> int:
    if n == 0:
        return 0
    times = 0
    m, r = divmod(n, 2)
    while r == 0:
        times += 1
        m, r = divmod(m, 2)
    return times


shiftableTimes = map(calcMaxShiftableTimes, numbers)
print(min(shiftableTimes))
