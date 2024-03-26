from unittest.mock import Mock, patch

from data.data_values import Values
from praktikum_dir.burger import Burger


class TestBurger:

    def test_get_price(self):

        mock_bun = Mock()
        mock_bun.get_price.return_value = Values.BUN_PRICE

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = Values.INGREDIENT_PRICE

        burger = Burger()

        burger.set_buns(mock_bun)

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        expected_price = Values.BUN_PRICE*2 + Values.INGREDIENT_PRICE*2

        assert burger.get_price() == expected_price
