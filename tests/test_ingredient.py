from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_ingredient_name(self):
        """Проверяем метод get_name()."""
        ingredient = Ingredient("sauce", "Ketchup", 0.5)
        assert ingredient.get_name() == "Ketchup"

    def test_ingredient_price(self):
        """Проверяем метод get_price()."""
        ingredient = Ingredient("filling", "Lettuce", 0.75)
        assert ingredient.get_price() == 0.75

    def test_ingredient_type(self):
        """Проверяем метод get_type()."""
        ingredient = Ingredient("sauce", "Mayo", 0.8)
        assert ingredient.get_type() == "sauce"

    def test_ingredient_invalid_type(self):
        """Проверяем, что не происходит ошибка при инициализации с невалидным типом."""
        ingredient = Ingredient("unknown_type", "Spice", 0.3)
        assert ingredient.get_type() == "unknown_type"

    def test_ingredient_string_name(self):
        """Проверяем, что имя ингредиента хранится как строка."""
        ingredient = Ingredient("filling", "Tomato", 0.6)
        assert isinstance(ingredient.get_name(), str)

    def test_ingredient_float_price(self):
        """Проверяем, что цена ингредиента хранится как float."""
        ingredient = Ingredient("sauce", "Barbecue", 1.25)
        assert isinstance(ingredient.get_price(), float)
