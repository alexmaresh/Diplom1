from praktikum.database import Database
import pytest


class TestDatabase:
    @pytest.mark.parametrize(
        "index, bun_name, bun_price",
        [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)],
    )
    def test_initial_buns(self, index, bun_name, bun_price):
        """Проверяем начальные булочки в базе данных."""
        db = Database()
        bun = db.buns[index]
        assert bun.name == bun_name and bun.price == bun_price

    @pytest.mark.parametrize(
        "index, ingredient_type, ingredient_name, ingredient_price",
        [
            (0, "SAUCE", "hot sauce", 100),
            (1, "SAUCE", "sour cream", 200),
            (2, "SAUCE", "chili sauce", 300),
            (3, "FILLING", "cutlet", 100),
            (4, "FILLING", "dinosaur", 200),
            (5, "FILLING", "sausage", 300),
        ],
    )
    def test_initial_ingredients(
        self, index, ingredient_type, ingredient_name, ingredient_price
    ):
        """Проверяем начальные ингредиенты в базе данных."""
        db = Database()
        ingredient = db.ingredients[index]
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    def test_count_buns_length_success(self):
        """Проверяем, что возвращаемый список булочек имеет правильную длину."""
        db = Database()
        assert len(db.available_buns()) == 3

    def test_count_ingredients_length_success(self):
        """Проверяем, что возвращаемый список ингредиентов имеет правильную длину."""
        db = Database()
        assert len(db.available_ingredients()) == 6
