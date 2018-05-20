# -*- coding: utf-8 -*-
# 整数の入力
a, b, c = map(int, input().split())
K = int(input())


def calcMaximumSum(a, b, c, K):
    maximum = max([a, b, c])
    if(maximum == a):
        return a * (2 ** K) + b + c
    elif(maximum == b):
        return a + b * (2 ** K) + c
    else:
        return a + b + c * (2 ** K)


print(calcMaximumSum(a, b, c, K))
