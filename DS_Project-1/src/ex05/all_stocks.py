import sys


def create_companies_stocks():
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return companies, stocks


def search_output(spisok: list):
    companies, stocks = create_companies_stocks()
    for elem in spisok:
        string = ''
        for key, value in companies.items():
            if key.lower() == elem.lower():
                price = stocks.get(value)
                string = f'{key} stock price is {price}'
                break
            elif value.lower() == elem.lower():
                string = f'{value} is a ticker symbol for {key}'
                break

        if string != '':
            print(string)
        else:
            print(f'{elem} is an unknown company or an unknown ticker symbol')


def all_stocks():
    if len(sys.argv) == 2:
        void = False
        spisok = sys.argv[1].replace(' ', '').split(sep=',')
        for elem in spisok:
            if elem == '':
                void = True
        if not void:
            search_output(spisok)
        else:
            pass
    else:
        pass


if __name__ == "__main__":
    all_stocks()
