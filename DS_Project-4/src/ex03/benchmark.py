#!/usr/bin/env python3

import timeit
import sys
from functools import reduce


def loop_func(setup: int, number: int) -> float:
    loop_func_code = '''
def loop_func(setup: int) -> int:
    result = 0
    for i in range(1, setup + 1):
        result = result + i * i
    return result
'''
    loop_func_time = timeit.timeit(stmt=loop_func_code, setup=setup, number=number)
    return loop_func_time


def reduce_func(setup: int, number: int) -> float:
    reduce_func_code = '''
def reduce_func(emails: list[str]) -> list[str]:
    result = reduce(lambda x, y: x + y * y, [i for i in range(1, setup + 1)])
    return result
'''
    reduce_func_time = timeit.timeit(stmt=reduce_func_code, setup=setup, number=number)
    return reduce_func_time


if __name__ == '__main__':

    if (len(sys.argv) == 4) and sys.argv[2].isdigit() and sys.argv[3].isdigit() :
        number = int(sys.argv[2])
        setup = sys.argv[3]
        if sys.argv[1] == 'loop':
            print(loop_func(setup, number))
        elif sys.argv[1] == 'reduce':
            print(reduce_func(setup, number))
        else:
            pass
