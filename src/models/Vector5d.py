from src.models.Point5d import Point5d

class vector_5d:
    p1 = Point5d(0, 0, 0, 0, 0)
    p2 = Point5d(0, 0, 0, 0, 0)
    module = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2