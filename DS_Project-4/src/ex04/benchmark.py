#!/usr/bin/env python3

import timeit


def my_func(setup: str, number: int) -> float:
    my_func_code = '''
def my_func(lst: list[int]) -> dict:
    my_dict = dict
    for i in range(101):
        n = 0
        for j in lst:
            if (j == i):
                n += 1
        my_dict[i] = n
    return my_dict
'''
    my_func_time = timeit.timeit(stmt=my_func_code, setup=setup, number=number)
    return my_func_time


def my_func_top(setup: str, number: int) -> float:
    my_func_top_code = '''
def my_func(lst: list[int]) -> dict:
    my_dict = dict
    for i in range(101):
        n = 0
        for j in lst:
            if (j == i):
                n += 1
        my_dict[i] = n
    my_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
    return my_dict[:10]
'''
    my_func_top_time = timeit.timeit(stmt=my_func_top_code, setup=setup, number=number)
    return my_func_top_time


def func(setup: str, number: int) -> float:
    func_code = '''
def func(lst: list[int]) -> dict:
    return dict(Counter(lst))
'''
    func_time = timeit.timeit(stmt=func_code, setup=setup, number=number)
    return func_time


def func_top(setup: str, number: int) -> float:
    func_top_code = '''
def func(lst: list[int]) -> dict:
    return dict(Counter(lst).most_common(10))
'''
    func_top_time = timeit.timeit(stmt=func_top_code, setup=setup, number=number)
    return func_top_time


if __name__ == '__main__':
    setup = '''
import random
from collections import Counter
lst = [random.randint(0, 100) for i in range(1000000)]
'''
    number = 10000000

    print(f'my function: {my_func(setup, number)}')
    print(f'Counter: {func(setup, number)}')
    print(f'my top: {my_func_top(setup, number)}')
    print(f'Counters top: {func_top(setup, number)}')