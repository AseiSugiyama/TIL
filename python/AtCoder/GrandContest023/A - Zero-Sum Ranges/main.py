# -*- coding: utf-8 -*-
from scipy.misc import comb
import collections

N = int(input())
numbers = map(int, input().split())


def countSubZeroRange(numbers):
    Sums = [0]
    for number in numbers:
        Sums.append(Sums[-1] + number)
    zeroSumCounts = 0
    for key, value in collections.Counter(Sums).items():
        zeroSumCounts += comb(value, 2, 1)
    return zeroSumCounts


print(countSubZeroRange(numbers))
