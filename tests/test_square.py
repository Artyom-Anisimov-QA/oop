from src.square import Square
import pytest

# Проверка площади квадрата позитив
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, area",
    [
     (5, 25),
     (3.5, 12.25)
    ],
    ids=["integer", "float"]
)
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.get_area == area, f"Площадь должна быть {area}"


# Проверки негатив квадрат
@pytest.mark.regression
def test_square_negative():
    with pytest.raises(ValueError, match="Стороны квадрата не могут быть меньше 0"):
        Square(-1)

# Введён неверный тип данных
@pytest.mark.regression
def test_square_negative():
    with pytest.raises(TypeError):
        Square("5")



# Проверка периметра квадрата
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "side_a, perimeter",
    [
        (5, 20),
        (5.5, 22)
    ],
    ids=["integer", "float"]
)
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert s.get_perimeter == perimeter, f"Периметр должен быть {perimeter}"


# Проверка равенства диагоналей квадрата
@pytest.mark.regression
@pytest.mark.parametrize("side_a", [(7), (7.5)], ids=["integer", "float"])
def test_square_diagonal_positive(side_a):
    s = Square(side_a)
    diag1 = s.get_diagonal_1
    diag2 = s.get_diagonal_2
    assert diag1 == diag2, "Диагонали квадрата должны быть равны"


# Проверка равенства сторон квадрата
@pytest.mark.regression
@pytest.mark.parametrize("side_a", [(7), (7.5)], ids=["integer", "float"])
def test_storony(side_a):
    s = Square(side_a)
    assert s.side_a == s.side_a, f"Стороны квадрата не равны"
