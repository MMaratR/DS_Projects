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


def ticker_symbols(companies: dict, stocks: dict):
    spisok = sys.argv[1:]

    if len(spisok) == 1:
        spisok = spisok[0].upper()
        price = stocks.get(spisok)

        if price != None:
            company = ''
            for key, value in companies.items():
                if value == spisok:
                    company = key
            print(company, price)
        else:
            print('Unknown company')
    else:
        pass


if __name__ == "__main__":
    companies, stocks = create_companies_stocks()
    ticker_symbols(companies, stocks)
