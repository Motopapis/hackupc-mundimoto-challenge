class Post():
    _brand = 0
    _model = 0
    _year = 0
    _fuel = 0
    _price = 0

    def __init__(self, brand=0, model=0, year=0, fuel=0, price=0):
        self._brand = brand
        self._model = model
        self._year = year
        self._fuel = fuel
        self._price = price

    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._year

    def get_fuel(self):
        return self._fuel

    def get_price(self):
        return self._price