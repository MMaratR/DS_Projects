#!/usr/bin/env python3
import sys
import os
import psutil


def func(path: str):
    file_exists = os.path.isfile(path)
    if not file_exists:
        raise Exception('Файла не существует')
    else:
        with open(path, 'r') as file:
            for line in file:
                yield line


def main() -> None:
    lines = func(sys.argv[1])
    for line in lines:
        pass

    usage = psutil.Process()
    print(f'Peak memory usage= {usage.memory_info().rss / (1024 * 1024 * 1024)} GB')
    print(f'User Mode Time + System Mode Time = {usage.cpu_times().user + usage.cpu_times().system}s')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        pass