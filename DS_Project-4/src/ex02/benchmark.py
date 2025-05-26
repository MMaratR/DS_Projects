#!/usr/bin/env python3

import timeit
import sys


def loop(setup: str, number: int) -> float:
    loop_code = '''
def loop(emails: list[str]) -> list[str]:
    gmails = []
    for email in emails:
        if email.endswith('@gmail.com'):
            gmails.append(email)
    return gmails
'''
    loop_time = timeit.timeit(stmt=loop_code, setup=setup, number=number)
    return loop_time


def list_comprehension(setup: str, number: int) -> float:
    list_comprehension_code = '''
def list_comprehension(emails: list[str]) -> list[str]:
    gmails = [email for email in emails if email.endswith('@gmail.com')]
    return gmails
'''
    list_comprehension_time = timeit.timeit(stmt=list_comprehension_code, setup=setup, number=number)
    return list_comprehension_time


def map_list(setup: str, number: int) -> float:
    map_list_code = '''
def map_list(emails: list[str]) -> list[str]:
    gmails = list(map(lambda email: email.endswith('@gmail.com'), emails))
    return gmails
'''
    map_list_time = timeit.timeit(stmt=map_list_code, setup=setup, number=number)
    return map_list_time


def filter_list(setup: str, number: int) -> float:
    filter_list_code = '''
def filter_list(emails: list[str]) -> list[str]:
    gmails = list(filter(lambda email: email.endswith('@gmail.com'), emails))
    return gmails
'''
    filter_list_time = timeit.timeit(stmt=filter_list_code, setup=setup, number=number)
    return filter_list_time


if __name__ == '__main__':
    setup = '''
emails = 5 * ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
'''

    if (len(sys.argv) == 3) and sys.argv[2].isdigit():
        number = int(sys.argv[2])
        if sys.argv[1] == 'loop':
            print(loop(setup, number))
        elif sys.argv[1] == 'list_comprehension':
            print(list_comprehension(setup, number))
        elif sys.argv[1] == 'map':
            print(map_list(setup, number))
        elif sys.argv[1] == 'filter':
            print(filter_list(setup, number))
        else:
            pass
