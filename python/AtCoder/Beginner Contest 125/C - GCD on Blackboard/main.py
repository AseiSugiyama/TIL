import numpy as np
from itertools import accumulate, chain, islice, starmap


def gcd_strategy():
    import math
    import fractions
    return math.gcd if hasattr(math, "gcd") else fractions.gcd


def calculate_maximum_subgcd_with_np_ufunc(numbers, gcd):
    gcd_ufunc = np.frompyfunc(gcd, 2, 1)
    cumgcds = gcd_ufunc.accumulate(numbers, dtype=np.object).astype(np.int)
    sub_cumgcds = np.roll(cumgcds, 1)
    sub_cumgcds[0] = 0
    reverse_cumgcds = gcd_ufunc.accumulate(
        numbers[::-1], dtype=np.object).astype(np.int)
    sub_reverse_cumgcds = np.roll(reverse_cumgcds, 1)
    sub_reverse_cumgcds[0] = 0
    return np.max(gcd_ufunc(sub_cumgcds, sub_reverse_cumgcds[::-1]))


def calculate_maximum_subgcd_with_func(numbers, gcd):
    cumgcds = accumulate(numbers, gcd)
    sub_cumgcds = islice(chain([0], cumgcds), len(numbers))
    reverse_cumgcds = accumulate(numbers[::-1], gcd)
    sub_reverse_cumgcds = islice(chain([0], reverse_cumgcds), len(numbers))
    sub_gcds = starmap(gcd, zip(sub_cumgcds, list(sub_reverse_cumgcds)[::-1]))
    return max(sub_gcds)


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    gcd = gcd_strategy()
    # calculate_maximum_subgcd = calculate_maximum_subgcd_with_np_ufunc
    calculate_maximum_subgcd = calculate_maximum_subgcd_with_func

    print(calculate_maximum_subgcd(numbers, gcd))
