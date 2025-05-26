import sys


def letter_starter(input_email):
    with open('employees.tsv', 'r') as file:
        lines = file.readlines()

    for line in lines[1:]:
        name, surname, email = line.strip('\n').split('\t')
        if email == input_email:
            return f"Уважаемый {name}, добро пожаловать в нашу команду. Мы уверены, что нам будет приятно работать с вами. Это обязательное условие для профессионалов, которых нанимает наша компания."

    return "Адрес электронной почты не найден."


if __name__ == "__main__":
    if len(sys.argv) == 2:
        message = letter_starter(sys.argv[1])
        print(message)
    else:
        pass
