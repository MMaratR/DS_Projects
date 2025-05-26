def data_types():
    result = [1, 'string', 1.1, True, [1, 2, 3],
              {'a': 1, 'b': 2}, (1, 2, 3), {1, 2, 3}]
    for i in range(len(result)):
        result[i] = type(result[i]).__name__

    print('[', end='')
    for i in range(len(result) - 1):
        print(result[i], end=', ')
    print(result[-1] + ']')


if __name__ == '__main__':
    data_types()
