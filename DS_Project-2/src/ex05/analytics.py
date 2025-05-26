import os
import random
import config as c


class Research():
    def __init__(self, file: str):
        self.file = file
        self.calc = self.Analytics()

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
        def __init__(self):
            self.count_0_1 = 0
            self.count_1_0 = 0
            self.count_0_1_pr = 0
            self.count_1_0_pr = 0

        def counts(self, result: list[list]):
            for lst in result:
                if lst == [0, 1]:
                    self.count_0_1 += 1
                if lst == [1, 0]:
                    self.count_1_0 += 1

        def fractions(self, result: list[list]):
            n = len(result)
            self.count_0_1_pr = self.count_0_1/n*100
            self.count_1_0_pr = self.count_1_0/n*100

    class Analytics(Calculations):

        def predict_random(self, count):
            lst = []
            for i in range(count):
                rand = random.randint(0, 1)
                if rand == 0:
                    lst.append([0, 1])
                if rand == 1:
                    lst.append([1, 0])
            return lst

        def predict_last(self, result: list[list]):
            return result[-1]

        def predict_count(self, result: list[list]):
            count_0_1, count_1_0 = 0, 0
            for lst in result:
                if lst == [0, 1]:
                    count_0_1 += 1
                if lst == [1, 0]:
                    count_1_0 += 1
            return count_0_1, count_1_0

        def save_file(self, result: list[list]):
            count_0_1, count_1_0 = self.predict_count(
                self.predict_random(c.num_of_steps))

            with open(f'./{c.out_file_name}.{c.expansion}', mode='w') as file:
                file.write(c.pattern.format(len(result), self.count_1_0,
                           self.count_0_1, round(self.count_1_0_pr, 2), round(self.count_0_1_pr, 2), count_1_0, count_0_1))
