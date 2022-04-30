from json import JSONEncoder


class Bike:
    def __init__(self, brand=None, model=None, year=None, fuel=None, price=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.price = price

    def to_safe_json(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "fuel": self.fuel,
            "price": self.price
        }