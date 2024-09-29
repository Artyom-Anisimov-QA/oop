from src.rectangle import Rectangle
import pytest

# Проверка площади прямоугольника позитив
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, side_d, area",
    [
     (3, 5, 3, 5, 15),
     (3.5, 5.5, 3.5, 5.5, 19.25)
    ],
    ids=["integer", "float"]
)
def test_rectangle_area_positive(side_a, side_b, side_c, side_d, area):
    r = Rectangle(side_a, side_b, side_c, side_d)
    assert r.get_area == area, f"Площадь должна быть {area}"


# Проверка прямоугольника негатив
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, side_d, error",
    [
        (-3, 5, -3, 5, ValueError),   # Отрицательные стороны
        (3, 0, 3, 0, ValueError),     # Нулевые сторонын
        ("a", 5, "a", 5, TypeError),  # Некорректные типы данных
    ],
    ids=["negative_sides", "zero_sides", "invalid_types"]
)
def test_rectangle_negative(side_a, side_b, side_c, side_d, error):
    with pytest.raises(error):
        Rectangle(side_a, side_b, side_c, side_d)


# Проверка периметра прямоугольника
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, side_d, perimeter",
    [
        (3, 5, 3, 5, 16),
        (3.5, 5.5, 3.5, 5.5, 18)
    ],
    ids=["integer", "float"]
)
def test_rectangle_perimeter_positive(side_a, side_b, side_c, side_d, perimeter):
    r = Rectangle(side_a, side_b, side_c, side_d)
    assert r.get_perimeter == perimeter, f"Периметр должен быть {perimeter}"


# Проверка равенства диагоналей прямоугольника
@pytest.mark.regression
@pytest.mark.parametrize("side_a, side_b, side_c, side_d", [(5, 7, 5, 7), (5.5, 7.5, 5.5, 7.5)], ids=["integer", "float"])
def test_rectangle_diagonal_positive(side_a, side_b, side_c, side_d):
    rect = Rectangle(side_a, side_b, side_c, side_d)
    diag1 = rect.get_diagonal_1
    diag2 = rect.get_diagonal_2
    assert diag1 == diag2, "Диагонали прямоугольника должны быть равны"


# Проверка равенства противоположных сторон прямоугольника
@pytest.mark.regression
@pytest.mark.parametrize("side_a, side_b, side_c, side_d", [(5, 7, 5, 7), (5.5, 7.5, 5.5, 7.5)], ids=["integer", "float"])
def test_rectangle_storony(side_a, side_b, side_c, side_d):
    rect = Rectangle(side_a, side_b, side_c, side_d)
    assert rect.side_a == rect.side_c, f"Противоположные стороны прямоугольника не равны"
    assert rect.side_b == rect.side_d, f"Противоположные стороны прямоугольника не равны"
