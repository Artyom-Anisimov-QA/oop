from src.figure import Figure


class Circle(Figure):  # создан класс Круг
    CONST_PI = 3.14

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f"Радиус не может быть меньше 0")
        self.radius = radius

    def __str__(self):
        return f"{self.__class__.__name__} (radius={self.radius})"  # строковый вывод свойств класса

    @property
    def get_perimeter(self):  # метод вычисления периметра круга
        return round(2 * self.CONST_PI * self.radius, 1)

    @property
    def get_area(self):  # метод вычисления прощади круга
        return round(self.CONST_PI * (self.radius**2), 1)


circle_1 = Circle(5.5)

print(f"circle_1: {circle_1}")
print(f"perimetr: {circle_1.get_perimeter}")
print(f"area: {circle_1.get_area}")
