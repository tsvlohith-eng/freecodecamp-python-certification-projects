class Rectangle:
    def __init__(self,width,height):
        self.height=height
        self.width=width
    def set_height(self,height):
        self.height=height
    def set_width(self,width):
        self.width=width
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.height+self.width)
    def get_diagonal(self):
        return ((self.height**2)+(self.width**2))**0.5
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return "Too big for picture."

        picture = ""

        for _ in range(self.height):
         picture += "*" * self.width + "\n"

        return picture
    def get_amount_inside(self, shape):
     return (self.width // shape.width) * (self.height // shape.height )
class Square(Rectangle):
    def __init__(self,side):
        self.height=side
        self.width=side
    def set_width(self,side):
        self.height=side
        self.width=side
    def set_height(self,side):
        self.height=side
        self.width=side
    def set_side(self,side):
        self.height=side
        self.width=side 
    def __str__(self):
        return f"Square(side={self.width})"