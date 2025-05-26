import config as c
import analytics as a

if __name__ == '__main__':
    research = a.Research(file=c.file_name)
    result = research.file_reader()
    # print(result)
    research.calc.counts(result)
    # print(research.calc.count_0_1, research.calc.count_1_0)
    research.calc.fractions(result)
    # print(research.calc.count_0_1_pr, research.calc.count_1_0_pr)
    # print(research.calc.predict_random(c.num_of_steps))
    # print(research.calc.predict_last(result))
    research.calc.save_file(result)
