# -*- coding: utf-8 -*-
H, W = map(int, input().split())
inputs = [input() for _ in range(H)]
canvas = [char for char in inputs]


def isSpace(canvas, i, j):
    if i in range(len(canvas)):
        if j in range(len(canvas[i])):
            return True if canvas[i][j] == "." else False
        else:
            return True
    else:
        return True


def isPaintableCanvasBySquare(canvas):
    H = len(canvas)
    W = len(canvas[0])
    for i, j in [(i, j) for i in range(H) for j in range(W)]:
        if(isSpace(canvas, i, j - 1) and
           isSpace(canvas, i, j + 1) and
           isSpace(canvas, i - 1, j) and
           isSpace(canvas, i + 1, j) and
           not isSpace(canvas, i, j)):
            return "No"
    return "Yes"


print(isPaintableCanvasBySquare(canvas))
