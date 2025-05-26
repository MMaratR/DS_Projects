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


def stock_prices(companies: dict, stocks: dict):
    spisok = sys.argv[1:]
    if len(spisok) == 1:
        try:
            company = companies[spisok[0]]
            price = stocks[company]
            print(company, price)
        except:
            print('Unknown company')
    else:
        pass


if __name__ == "__main__":
    companies, stocks = create_companies_stocks()
    stock_prices(companies, stocks)
