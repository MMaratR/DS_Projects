import sys
import os


class Research():
    def __init__(self, file: str):
        self.file = file
        self.calc = self.Calculations()

    def check_struct(self, lines: list[str]):
        has_header = True
        if len(lines[0].split(',')) == 2 and (len(lines) != 1 or len(lines) != 0):

            a, b = lines[0].strip('\n').split(',')
            if (a == '0' or a == '1') and (b == '0' or b == '1') and a != b:
                has_header = False

            if has_header:
                lines = lines[1:]

            for line in lines:
                try:
                    a, b = line.strip('\n').split(',')
                    if (a == '0' or a == '1') and (b == '0' or b == '1') and a != b:
                        continue
                    else:
                        raise
                except:
                    raise Exception('Не верные данные')

            return has_header
        else:
            raise Exception('Файл с другой структурой')

    def file_reader(self):
        if not os.path.isfile(self.file):
            raise Exception(f"Файл {self.file} не найден.")

        with open(f'{self.file}', mode='r', encoding='utf-8') as file:
            result = []
            lines = file.readlines()
            has_header = self.check_struct(lines)

            if has_header:
                lines = lines[1:]

            for line in lines:
                result.append(list(map(int, line.strip('\n').split(','))))
            return result

    class Calculations():

        def counts(self, result: list[list]):
            count_0_1, count_1_0 = 0, 0
            for lst in result:
                if lst == [0, 1]:
                    count_0_1 += 1
                if lst == [1, 0]:
                    count_1_0 += 1
            return count_0_1, count_1_0

        def fractions(self, result: list[list]):
            n = len(result)
            count_0_1, count_1_0 = self.counts(result)
            return (count_0_1/n*100), (count_1_0/n*100)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        research = Research(file=sys.argv[1])
        result = research.file_reader()
        print(result)
        print(research.calc.counts(result))
        print(research.calc.fractions(result))
    else:
        pass
