from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_height(self, height):
        return self.set_side(height)
    
    def set_width(self, width):
        return self.set_side(width)


