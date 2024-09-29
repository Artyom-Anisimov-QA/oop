from src.circle import Circle
import pytest

#Тест метода вычисления площади круга
@pytest.mark.smoke
@pytest.mark.regression
def test_circle_area():
    c = Circle(5)
    assert c.get_area == 78.5


#Проверка площади круга
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "radius, area",
    [
     (5, 78.5),
     (5.5, 95.0)
    ],
    ids=["integer", "float"]
)
def test_circle_area1(radius, area):
    c = Circle(radius)
    assert c.get_area == area, f"Площать круга равна {area}"



#Тест метода вычисления периметра круга
@pytest.mark.smoke
@pytest.mark.regression
def test_circle_perimeter():
    c =Circle(5)
    assert c.get_perimeter == 31.4


#Проверка периметра круга
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "radius, perimeter",
    [
     (5, 31.4),
     (5.5, 34.5)
    ],
    ids=["integer", "float"]
)
def test_circle_area1(radius, perimeter):
    c = Circle(radius)
    assert c.get_perimeter == perimeter, f"Периметр круга равен {perimeter}"


#Проверка круга негатив
@pytest.mark.regression
@pytest.mark.parametrize(
    "radius, error",
    [
        (-3,  ValueError),   # Отрицательный радиус
        (0, ValueError),     # Радиус равен 0
        ("5", TypeError),  # Некорректные типы данных
    ],
    ids=["negative_radius", "zero_radius", "invalid_types"]
)
def test_circle_negative(radius, error):
    with pytest.raises(error):
        Circle(radius)


