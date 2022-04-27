from api import get_api_data
from services import find_most_volatile_stock, write_stock_to_csv


def start():
    data = get_api_data(['AAPL', 'AMZN', 'NFLX', 'FB', 'GOOGL'])
    most_volatile_stock = find_most_volatile_stock(data)
    write_stock_to_csv(most_volatile_stock)


if __name__ == "__main__":
    start()
