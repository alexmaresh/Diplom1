from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_burger_add_bun_success(self):
        """Проверяем, что бургер правильно создается с булочкой"""
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient_success(self):
        """Проверяем, что бургер правильно создается с ингредиентами"""
        burger = Burger()
        mock_ingr_1 = Mock()
        mock_ingr_2 = Mock()
        burger.add_ingredient(mock_ingr_1)
        burger.add_ingredient(mock_ingr_2)
        assert len(burger.ingredients) == 2 and burger.ingredients == [
            mock_ingr_1,
            mock_ingr_2,
        ]

    def test_delete_ingredient_success(self):
        """Проверяем, что из бургеров правильно удаляется ингредиент"""
        burger = Burger()
        mock_ingr_1 = Mock()
        mock_ingr_2 = Mock()
        burger.add_ingredient(mock_ingr_1)
        burger.add_ingredient(mock_ingr_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient_success(self):
        """Проверяем перемещение ингредиента."""
        burger = Burger()
        mock_ingr_1 = Mock()
        mock_ingr_2 = Mock()
        burger.add_ingredient(mock_ingr_1)
        burger.add_ingredient(mock_ingr_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingr_2, mock_ingr_1]

    def test_get_price_success(self):
        """Проверяем правильность расчета цены бургера."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 15
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 100 * 2 + 15

    def test_get_receipt_success(self):
        """Проверяем правильность формата чека."""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Круглая булка"
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "Соус"
        mock_ingredient.get_name.return_value = "Сыр"
        mock_bun.get_price.return_value = 49.99
        mock_ingredient.get_price.return_value = 11.1
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_receipt = "(==== Круглая булка ====)\n= соус Сыр =\n(==== Круглая булка ====)\n\nPrice: 111.08"
        assert burger.get_receipt() == expected_receipt
