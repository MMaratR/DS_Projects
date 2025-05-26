import config as c
import analytics as a

if __name__ == '__main__':
    research = a.Research(file=c.file_name)
    result = research.file_reader()
    research.calc.counts(result)
    research.calc.fractions(result)
    research.calc.save_file(result)
