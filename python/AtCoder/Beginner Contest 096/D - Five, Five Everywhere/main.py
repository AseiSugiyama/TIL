# -*- coding: utf-8 -*-
# 整数の入力
import math
N = int(input())


# primes from [Pythonで素数列挙と素数判定 - Qiita](https://qiita.com/neko_the_shadow/items/4ebad619564a48f5a97f)
def calcPrimes(x):
    if x < 2:
        return []
    primes = [i for i in range(x)]
    primes[1] = 0
    for prime in primes:
        if prime > math.sqrt(x):
            break
        if prime == 0:
            continue
        for non_prime in range(2 * prime, x, prime):
            primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


# is_prime from [Pythonで素数列挙と素数判定 - Qiita](https://qiita.com/neko_the_shadow/items/4ebad619564a48f5a97f)
def isPrime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True  # 2,3,5は素数
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0:
            return False
        prime += step
        step = 6 - step
    return True


def calcFiveFivePrimes(N):
    primes = calcPrimes(2000)
    fiveFivePrimes = [prime for prime in primes if prime % 5 == 1]
    return fiveFivePrimes[:N]


print(" ".join(map(str, calcFiveFivePrimes(N))))
