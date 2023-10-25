from Shapes import Ellipse, N_gon

<<<<<<< Updated upstream
ellipsis1 = Ellipse(1, 1)
ellipsis2 = Ellipse(1, 2)
print(f"Это круг? {ellipsis1.is_circle()}")
print(f'Площадь {ellipsis2.area()}')
print(f"Эксцентриситет {ellipsis1.eccentricity()}")
=======
elips1 = Ellipse(1, 1)
elips2 = Ellipse(1, 2)
print(f"Это круг? {elips1.is_circle()}")
print(f'Площадь {elips2.area()}')
print(f"Эксцентриситет {elips1.eccentricity()}")
>>>>>>> Stashed changes

triangle = N_gon(3, [1, 2, 3], [60, 90, 30])
print(f"Треугольник вырожденый? {triangle.is_degenerate()}")

square = N_gon(4, [2, 2, 2, 2], [90] * 4)
print(f"Четырёхугольник выпуклый? {square.is_convex()}")

pentagon = N_gon(5, [2, 4, 5, 6, 7], [0] * 5)
print(f"Периметр пятиугольника {pentagon.c_perimeter()}")
