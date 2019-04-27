from main import (calculate_maximum_subgcd_with_func,
                  calculate_maximum_subgcd_with_np_ufunc,
                  gcd_strategy)
import numpy as np
gcd = gcd_strategy()


def test_calculate_maximum_subgcd_with_func_case_1():
    numbers = [2, 4, 8, 8]
    assert calculate_maximum_subgcd_with_func(numbers, gcd) == 4


def test_calculate_maximum_subgcd_with_func_case_2():
    numbers = [7, 6, 8]
    assert calculate_maximum_subgcd_with_func(numbers, gcd) == 2


def test_calculate_maximum_subgcd_with_func_case_3():
    numbers = [12, 15, 18]
    assert calculate_maximum_subgcd_with_func(numbers, gcd) == 6


def test_calculate_maximum_subgcd_with_func_case_4():
    numbers = [1000000000, 1000000000]
    assert calculate_maximum_subgcd_with_func(numbers, gcd) == 1000000000


def test_calculate_maximum_subgcd_with_np_ufunc_case_1():
    numbers = np.array([2, 4, 8, 8])
    assert calculate_maximum_subgcd_with_np_ufunc(numbers, gcd) == 4


def test_calculate_maximum_subgcd_with_np_ufunc_case_2():
    numbers = np.array([7, 6, 8])
    assert calculate_maximum_subgcd_with_np_ufunc(numbers, gcd) == 2


def test_calculate_maximum_subgcd_with_np_ufunc_case_3():
    numbers = np.array([12, 15, 18])
    assert calculate_maximum_subgcd_with_np_ufunc(numbers, gcd) == 6


def test_calculate_maximum_subgcd_with_np_ufunc_case_4():
    numbers = np.array([1000000000, 1000000000])
    assert calculate_maximum_subgcd_with_np_ufunc(numbers, gcd) == 1000000000
