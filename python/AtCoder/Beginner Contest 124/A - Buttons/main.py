A, B = map(int, input().split())
# A, B = 6, 6


def calc_maximum_coins(A, B):
    if A > B:
        s, t, result = A - 1, B, A
    else:
        s, t, result = A, B - 1, B

    return result + max(s, t)


print(calc_maximum_coins(A, B))