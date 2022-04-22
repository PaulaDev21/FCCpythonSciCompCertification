from math import trunc


class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2*(self.height + self.width)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        MAX_SIDE = 50

        if self.width > MAX_SIDE or self.height > MAX_SIDE:
            return "Too big for picture."
        pic = ''
        print(self.width, self.height)
        for i in range(0, self.height):
            for j in range(0, self.width):
                pic += "*"
            pic += '\n'
        return pic[0:len(pic)-1]

    def get_amount_inside(self, insider_rect):
        if insider_rect.get_width() > self.width or insider_rect.get_height() > self.height:
            return 0

        n_vertical = trunc(self.width / insider_rect.get_width())
        n_horizontal = trunc(self.height / insider_rect.get_height())

        return n_vertical * n_horizontal

# ------------- FAST TESTS ---------------


r = Rectangle(5, 3)
print(r.get_diagonal())
print(r.get_area())
print(r.get_picture())

r2 = Rectangle(0.6, 2.2)

print(r, r2)

print(r.get_amount_inside(r2))
