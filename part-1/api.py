import requests


def get_api_data(stocks):
    data = []

    for stock in stocks:
        result = requests.get('https://finnhub.io/api/v1/quote',
                              params={'symbol': stock},
                              headers={'X-Finnhub-Token': 'c9kramqad3ifl3rgqo9g'}).json()
        result['symbol'] = stock
        data.append(result)

    return data
