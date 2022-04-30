from json import JSONEncoder

class Brand():
    def __init__(self, name=None, models=None):
        self.name = name
        self.models = models

    def to_safe_json(self):
        return {
            "name": self.name,
            "models": self.models
        }