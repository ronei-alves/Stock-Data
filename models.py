class Stock:
    def __init__(self, ticker, country, price='get_price'):
        self._ticker = ticker
        self._country = country
        self._price = price

    # Getter and Setters
    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        self._ticker = ticker

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        self._country = country

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
