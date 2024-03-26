from unittest.mock import Mock

from data.data_values import Values
from praktikum_dir.burger import Burger


class TestBurger:

    def test_get_price(self, mocked_bun, mocked_ingredient):

        burger = Burger()

        burger.set_buns(mocked_bun)

        burger.add_ingredient(mocked_ingredient)
        burger.add_ingredient(mocked_ingredient)

        expected_price = Values.BUN_PRICE * 2 + Values.INGREDIENT_PRICE * 2

        assert burger.get_price() == expected_price

    def test_get_receipt(self, mocked_bun, mocked_ingredient):

        burger = Burger()

        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        burger.add_ingredient(mocked_ingredient)

        assert burger.get_receipt() == Values.EXPEXTED_RECEIPT
