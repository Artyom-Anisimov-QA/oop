from src.triangle import Triangle
import pytest

# Проверка площади треугольника позитив
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
     (5, 6, 7, 14.7),
     (5.5, 6.5, 7.5, 17.4)
    ],
    ids=["integer", "float"]
)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area, f"Площадь должна быть {area}"

#Тест метода вычисления площади треугольника
@pytest.mark.smoke
@pytest.mark.regression
def test_area_triangle():
    t =Triangle(5.5, 6.5, 7.5)
    assert t.get_area == 17.4


#Проверка треугольника негатив
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, error",
    [
        (-3, 5, -4, ValueError),   # Отрицательные стороны
        (3, 0, 3, ValueError),     # Нулевые сторонын
        ("a", 5, "5", TypeError),  # Некорректные типы данных
    ],
    ids=["negative_sides", "zero_sides", "invalid_types"]
)
def test_triangle_negative(side_a, side_b, side_c, error):
    with pytest.raises(error):
        Triangle(side_a, side_b, side_c)


# Проверка периметра треугольника
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter",
    [
        (5, 6, 7, 18),
        (5.5, 6.5, 7.5, 19.5)
    ],
    ids=["integer", "float"]
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter, f"Периметр должен быть {perimeter}"


# Проверка полуперимтера периметра треугольника
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimeter",
    [
        (5, 6, 7, 18),
        (5.5, 6.5, 7.5, 19.5)
    ],
    ids=["integer", "float"]
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    poluperimeter = t.get_perimeter / 2
    exp_poluperimeter = perimeter /2
    assert exp_poluperimeter == poluperimeter, f"Полумериметр треугольника равер {exp_poluperimeter}"


# Тест для валидных треугольников
@pytest.fixture
def valid_triangles():
    return [
        (3, 4, 5),
        (5, 6, 7),
        (10, 10, 10)
    ]

@pytest.mark.smoke
@pytest.mark.regression

def test_valid_triangles(valid_triangles):
    for side_a, side_b, side_c in valid_triangles:
        assert Triangle(side_a, side_b, side_c), f"Треугольник со сторонами {side_a}, {side_b}, {side_c} должен быть валидным"
