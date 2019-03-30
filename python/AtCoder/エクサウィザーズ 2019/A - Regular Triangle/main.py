A, B, C = map(int, input().split())


def canExistRegularTriangle(A, B, C):
    return (A == B) and (B == C) and (C == A)


def printAbleToExistRegularTriangle(A, B, C):
    if canExistRegularTriangle(A, B, C):
        print("Yes")
    else:
        print("No")


printAbleToExistRegularTriangle(A, B, C)