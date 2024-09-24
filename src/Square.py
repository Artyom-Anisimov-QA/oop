from src.Rectangle import Rectangle


class Square(Rectangle):  # создан класс Square(наследник класса Rectangle)
    def __init__(self, side_a):  # инициализированы параметры класса
        if side_a <= 0:
            raise ValueError("Стороны квадрата не могут быть меньше 0")
        super().__init__(
            side_a, side_a
        )  # получение доступа до методов и атрибутов родительского класса (Rectangle)
        self.side_a = side_a  # сторона а

    def __str__(self):
        return f"{self.__class__.__name__} (a={self.side_a}, b={self.side_a})"  # строковый вывод свойств класса


square_1 = Square(5)


print(f"Square 1: {square_1}")
print(f"area = {square_1.get_area}")
print(f"perimetr = {square_1.get_perimeter}")
