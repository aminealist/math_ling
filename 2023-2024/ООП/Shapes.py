from math import pi


class N_gon:
    def __init__(self, n_of_sides, sides, angles):
        self.n_of_sides = n_of_sides
        self.sides = sorted(sides)
        self.angles = sorted(angles)

    def c_perimeter(self):
        return sum(self.sides)

    def is_convex(self):
        return 1 if max(self.angles) < 180 else 0

    def is_degenerate(self):
        return 1 if 2 * max(self.sides) == sum(self.sides) else 0


class Ellipse:
    def __init__(self, h_radius, v_radius):
        self.h_radius, self.v_radius = min(h_radius, v_radius), max(h_radius, v_radius)

    def area(self):
        return pi * self.h_radius * self.v_radius

    def eccentricity(self):
        return round((1 - self.v_radius ** 2 / self.h_radius ** 2) ** 0.5, 5)

    def is_circle(self):
        return 1 if self.v_radius == self.h_radius else 0

