import sys
import os


class Research():
    def __init__(self, file: str):
        self.file = file

    def check_struct(self, lines: list[str]):
        if len(lines[0].split(',')) == 2 and len(lines) != 1:
            for line in lines[1:]:
                try:
                    a, b = line.strip('\n').split(',')
                    if (a == '0' or a == '1') and (b == '0' or b == '1') and a != b:
                        continue
                    else:
                        raise
                except:
                    raise Exception('Не верные данные')
        else:
            raise Exception('Файл с другой структурой')

    def file_reader(self):
        if not os.path.isfile(self.file):
            raise Exception(f"Файл {self.file} не найден.")

        with open(f'{self.file}', mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            self.check_struct(lines)
            file.seek(0)
            return file.read()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        research = Research(file=sys.argv[1])
        print(research.file_reader())
    else:
        pass
