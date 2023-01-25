class Rectangle:
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

main_rect = Rectangle(5, 4)
print(main_rect.area())