class Rectangle:
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle:
    def __int__(self, r):
        self.r = r


main_rect = Rectangle(5, 4)
print(main_rect.area())
main_circle = Circle(2)