from src.figure import Figure


class Triangle(Figure):  # создан класс Треугольник
    def __init__(self, side_a, side_b, side_c):  # инициализированы параметры класса
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника не могут быть меньше 0")
        if (side_a + side_b < side_c) or (side_a + side_c < side_b) or (side_b + side_c < side_a):
            raise ValueError("Длина любой стороны треугольника всегда меньше суммы длин двух его других сторон")

        self.side_a = side_a  # сторона а
        self.side_b = side_b  # сторона b
        self.side_c = side_c  # сторона с

    def __str__(self):
        return f"{self.__class__.__name__} (a={self.side_a}, b = {self.side_b}, c = {self.side_c})"  # строковый вывод свойств класса

    @property
    def get_perimeter(self):  # метод вычисления периметра Triangle
        return self.side_a + self.side_b + self.side_c

    def get_poluperimeter(self):
        return triangle_1.get_perimeter / 2

    @property
    def get_area(self):  # метод вычисления прощади Triangle
        from math import sqrt
        return round(sqrt(triangle_1.get_poluperimeter() * (triangle_1.get_poluperimeter() - self.side_a) * (triangle_1.get_poluperimeter() - self.side_b) * (triangle_1.get_poluperimeter() - self.side_c)), 1,)  # формула Герона


triangle_1 = Triangle(5.5, 6.5, 7.5)  # создан экземпляр класса


#print(f"Triangle 1:  {triangle_1}")
#print(f"perimeter: {triangle_1.get_perimeter}")
print(f"poluperimeter: {triangle_1.get_poluperimeter()}")
print(f"area: {triangle_1.get_area}")
