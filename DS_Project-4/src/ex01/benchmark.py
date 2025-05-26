#!/usr/bin/env python3

import timeit


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


if __name__ == '__main__':
    setup = '''
emails = 5 * ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
'''
    number = 9000000

    loop_time = loop(setup, number)
    list_comprehension_time = list_comprehension(setup, number)
    map_list_time = map_list(setup, number)

    if list_comprehension_time < loop_time and list_comprehension_time < map_list_time:
        print('it is better to use a list comprehension')
    elif loop_time < list_comprehension_time and loop_time < map_list_time:
        print('it is better to use a loop')
    elif map_list_time < loop_time and map_list_time < list_comprehension_time:
        print('it is better to use a map')

    print(f'{loop_time} vs {list_comprehension_time} vs {map_list_time}')
