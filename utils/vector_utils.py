from src.models.Vector5d import vector_5d
from src.models.Point5d import Point5d
from math import pow, sqrt

class VectorUtils:

    @staticmethod
    def compute_module(vector):
        p1 = vector.p1
        p2 = vector.p2

        x2 = pow(p2.x-p1.x, 2)
        y2 = pow(p2.y-p1.y, 2)
        z2 = pow(p2.z-p1.z, 2)
        i2 = pow(p2.i-p1.i, 2)
        j2 = pow(p2.j-p1.j, 2)

        return sqrt(x2 + y2 + z2 + i2 + j2)

    @staticmethod
    def generate_vector(point1, point2):
        return vector_5d(point1, point2)