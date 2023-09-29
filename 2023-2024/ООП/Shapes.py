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


elips1 = Ellipse(1, 1)
elips2 = Ellipse(1, 2)
print(f"Это круг? {elips1.is_circle()}")
print(f'Площадь {elips2.area()}')
print(f"Эксцентриситет {elips1.eccentricity()}")


triangle = N_gon(3, [1, 2, 3], [60, 90, 30])
print(f"Треугольник вырожденый? {triangle.is_degenerate()}")

square = N_gon(4, [2, 2, 2, 2], [90] * 4)
print(f"Четырёхугольник выпуклый? {square.is_convex()}")

pentagon = N_gon(5, [2, 4, 5, 6, 7], [0] * 5)
print(f"Периметр пятиугольника {pentagon.c_perimeter()}")
