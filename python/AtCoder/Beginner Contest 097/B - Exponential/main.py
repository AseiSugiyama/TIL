# -*- coding: utf-8 -*-
X = int(input())


def exponential(X):
    value = 1
    for n in range(34):
        for p in range(2, 10):
            tmp = n ** p
            if tmp > X:
                break
            else:
                value = max(value, tmp)
    return value


print(exponential(X))
