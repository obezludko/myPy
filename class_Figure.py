class Figure:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        print('Figure')
        print('Color: ' + self.color)

figu = Figure('white')
print(figu.get_color())
print(figu.info())
print('\n\n')


class Rectangle(Figure):
    def __init__(self,color,width = 100, height = 100):
        super().__init__(color)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: "  + str(self.width))
        print("Height: " + str(self.height))
        print("Square: " + str(self.square()))

fig1 = Figure('green')
print(fig1.info())
rect1 = Rectangle('red',54,34)
print(rect1.info())