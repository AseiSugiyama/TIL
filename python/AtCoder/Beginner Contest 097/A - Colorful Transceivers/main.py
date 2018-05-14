# -*- coding: utf-8 -*-
a, b, c, d = map(int, input().split())


def isTalkable(a, b, c, d):
    if abs(a - c) <= d:
        return "Yes"
    elif(abs(a - b) <= d) and (abs(b - c) <= d):
        return "Yes"
    else:
        return "No"


print(isTalkable(a, b, c, d))
