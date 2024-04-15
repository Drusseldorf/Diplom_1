from praktikum_dir.ingredient import Ingredient
from data.data_values import Values


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(Values.INGREDIENT_TYPE,
                                Values.INGREDIENT_NAME,
                                Values.INGREDIENT_PRICE)
        assert ingredient.get_price() == Values.INGREDIENT_PRICE

    def test_get_name(self):
        ingredient = Ingredient(Values.INGREDIENT_TYPE,
                                Values.INGREDIENT_NAME,
                                Values.INGREDIENT_PRICE)
        assert ingredient.get_name() == Values.INGREDIENT_NAME

    def test_get_type(self):
        ingredient = Ingredient(Values.INGREDIENT_TYPE,
                                Values.INGREDIENT_NAME,
                                Values.INGREDIENT_PRICE)
        assert ingredient.get_type() == Values.INGREDIENT_TYPE
