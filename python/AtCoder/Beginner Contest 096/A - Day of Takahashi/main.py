# -*- coding: utf-8 -*-
a, b = map(int, input().split())


def countTakahashiDays(a, b):
    return a - 1 + (1 if b >= a else 0)


print(countTakahashiDays(a, b))
