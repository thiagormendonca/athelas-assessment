def find_most_volatile_stock(stocks):
    most_volatile_stock = None
    most_volatile_value = 0

    for stock in stocks:
        if abs(stock['dp']) > most_volatile_value:
            most_volatile_stock = stock
            most_volatile_value = stock['dp']

    return most_volatile_stock


def write_stock_to_csv(stock):
    with open('output.csv', 'w') as f:
        f.write('stock_symbol,percentage_change,current_price,last_close_price\n')
        f.write('{}, {}, {}, {}\n'.format(
            stock['symbol'],
            stock['dp'],
            stock['c'],
            stock['pc']
        ))
