class Stock:
    def __init__(self, name):
        self.__name = name
        self.__price_history = []

    def get_name(self):
        return self.__name

    def update_price(self, price):
        self.__price_history.append(price)

    def get_current_price(self):
        return self.__price_history[-1]

    def get_last_7days_prices(self):
        return self.__price_history[-7:]
