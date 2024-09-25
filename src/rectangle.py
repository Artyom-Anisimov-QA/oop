from src.figure import Figure


class Rectangle(Figure):  # создан класс Прямоугольник
    def __init__(self, side_a, side_b):  # инициализированы параметры класса
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника не могут быть меньше 0")
        self.side_a = side_a  # сторона а
        self.side_b = side_b  # сторона b

    def __str__(self):
        return f"{self.__class__.__name__} (a={self.side_a}, b = {self.side_b})"  # строковый вывод свойств класса

    @property
    def get_area(self):  # метод вычисления прощади Rectangle
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):  # метод вычисления периметра Rectangle
        return (self.side_a + self.side_b) * 2


rectangle_1 = Rectangle(3, 5)  # создан экземпляр класса


print(f"Rectangle 1:  {rectangle_1}")
print(f"area: {rectangle_1.get_area}")  # вызов метода, как атрибута класса Rectangle
print(f"perimeter: {rectangle_1.get_perimeter}")  # вызов метода, как атрибута класса Rectangle
