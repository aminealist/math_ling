class Figure:
    def __init__(self, color="White"):
        self.color = color

    def change_color(self, color):
        self.color = color


class Ellipse(Figure):
    def __init__(self, r1, r2, color="White"):
        super().__init__(color)
        self.h_radius, self.v_radius = min(r1, r2), max(r1, r2)

    def parameters(self):
        print("ellipse", self.color)


class Square(Figure):
    def __init__(self, a, color="white"):
        super().__init__(color)
        self.square_side = a

    def parameters(self):
        print("square", self.color)



