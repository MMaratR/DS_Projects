#!/usr/bin/env python3

import sys
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import httpx
import cProfile
import pstats


def financial(tiker: str, field: str) -> tuple:
    found = False
    url = f'https://finance.yahoo.com/quote/{tiker.upper()}/financials/?p={tiker.lower()}'
    headers = {
        'Accept': '*/*',
        'User-Agent': UserAgent().random
    }
    req = httpx.get(url, headers=headers)
    if req.status_code != 200:
        raise Exception(f'Ошибка запроса: {req.status_code}')

    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    if soup.find(class_='noData yf-wnifss'):
        raise Exception(f'Тикер {tiker} не найден')

    for elem in soup.find_all(class_='row lv-0 yf-t22klz'):
        if elem.find(class_='rowTitle yf-t22klz').text.strip() == field:
            found = True
            elems = elem.find_all(class_='yf-t22klz')
            result = [element.text.replace('.00 ', '') for element in elems]
            result = result[1:]
            break

    if found:
        return tuple(result)
    else:
        raise Exception(f'Поле {field} не найденно')


if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    if len(sys.argv) == 3:
        result = financial(sys.argv[1], sys.argv[2])
        print(result)
    else:
        raise Exception('Много переменных')
    profiler.disable()

    with open('pstats-cumulative.txt', 'w') as file:
        pstats.Stats(profiler, stream=file).strip_dirs().sort_stats('cumulative').print_stats(5)
