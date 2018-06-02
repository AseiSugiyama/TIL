# -*- coding: utf-8 -*-
A, B, C, K = map(int, input().split())


def calcFairness(A, B, K):
    if abs(A - B) > 10 ** 18:
        return 'unfair'
    else:
        return ((-1) ** (K % 2)) * (A - B)


print(calcFairness(A, B, K))
