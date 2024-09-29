from src.figure import Figure
from src.rectangle import Rectangle
from src.triangle import Triangle
import pytest

#Тест проверки метода add_area()
def test_add_area():
    rect = Rectangle()
    tri = Triangle()

    figura_1 = rect.get_area()
    figura_2 = tri.get_area()
    add_figura = figura_1 + figura_2
    assert Figure.add_area(figura_1, figura_2) == add_figura



