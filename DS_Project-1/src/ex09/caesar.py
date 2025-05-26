import sys


def caesar_cipher(text: str, shift: int, mode: bool):
    new_text = ''

    if mode:
        for elem in text:
            if 97 <= ord(elem) <= 122 and ord(elem) + shift > 122:
                new_text += chr(ord(elem) + shift - 26)
            elif 97 <= ord(elem) <= 122 and ord(elem) + shift <= 122:
                new_text += chr(ord(elem) + shift)
            else:
                new_text += elem
    else:
        for elem in text:
            if 97 <= ord(elem) <= 122 and ord(elem) - shift < 97:
                new_text += chr(ord(elem) - shift + 26)
            elif 97 <= ord(elem) <= 122 and ord(elem) - shift >= 97:
                new_text += chr(ord(elem) - shift)
            else:
                new_text += elem

    print(new_text)


def caesar():
    mode = sys.argv[1]
    text = sys.argv[2]

    for elem in text:
        if 1072 <= ord(elem) <= 1103:
            raise Exception('Скрипт пока не поддерживает ваш язык')

    try:
        shift = int(sys.argv[3])
    except:
        raise ValueError('Сдвиг должен быть целым числом')

    if mode == 'encode':
        caesar_cipher(text, shift, True)
    elif mode == 'decode':
        caesar_cipher(text, shift, False)
    else:
        raise Exception('Нет такого действия')


if __name__ == "__main__":
    if len(sys.argv) == 4:
        caesar()
    else:
        raise Exception('Не правильное количество аргументов')
