from math import pi
from math import sqrt


class N_gon:
    def __init__(self, n_of_sides, sides, angles):
        self.n_of_sides = n_of_sides
        self.sides = sorted(sides)
        self.angles = sorted(angles)

    def c_perimeter(self):
        return sum(self.sides)

    def is_convex(self):
        return True if max(self.angles) < 180 else False

    def is_degenerate(self):
        return True if 2 * max(self.sides) == sum(self.sides) else False


class Ellipse:
    def __init__(self, h_radius, v_radius):
        self.h_radius, self.v_radius = min(h_radius, v_radius), max(h_radius, v_radius)

    def area(self):
        return round(pi * self.h_radius * self.v_radius, 3)

    def eccentricity(self):
        return round(sqrt(1 - self.h_radius ** 2 / self.v_radius ** 2), 3)

    def is_circle(self):
        return True if self.v_radius == self.h_radius else False



