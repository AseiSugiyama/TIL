# -*- coding: utf-8 -*-
A, B = map(int, input().split())


def calcMaxAddSubMul(A, B):
    return max([A+B, A-B, A*B])


print(calcMaxAddSubMul(A, B))