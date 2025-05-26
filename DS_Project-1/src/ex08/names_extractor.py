import sys


def name_extractor(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    employees = []

    for line in lines:
        email = line.strip('\n')
        if email:
            name, surname = email.split('@')[0].split('.')
            name = name.capitalize()
            surname = surname.capitalize()
            employees.append(f"{name}\t{surname}\t{email}")

    with open('employees.tsv', 'w') as output_file:
        output_file.write("Name\tSurname\tE-mail\n")
        output_file.write("\n".join(employees) + "\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        name_extractor(sys.argv[1])
    else:
        pass
