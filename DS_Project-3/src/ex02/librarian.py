import os


def main():
    env = os.environ.get('VIRTUAL_ENV')
    if (os.path.basename(env) != "oswynsea"):
        raise KeyError('Не правильная среда')

    os.system("pip install -r requirements.txt")
    os.system("pip freeze > requirements.txt")
    os.system("zip -r oswynsea.zip ../oswynsea")


if __name__ == '__main__':
    try:
        main()
    except KeyError as error:
        print(error)
