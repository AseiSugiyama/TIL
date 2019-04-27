A, B, T = map(int, input().split())
# A, B, T = 20, 20, 19


def count_total_biscuit(A, B, T):
    return (T // A) * B


print(count_total_biscuit(A, B, T))
