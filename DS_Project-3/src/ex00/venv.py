import os


def venv_test():
    env = os.environ.get('VIRTUAL_ENV')
    print(f'Your current virtual env is {env}')


if __name__ == '__main__':
    venv_test()


# python3 -m venv oswynsea
# source oswynsea/bin/activate
# deactivate
