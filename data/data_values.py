class Values:

    BUN_NAME = 'Булочка с маком'
    BUN_PRICE = 100
    BUN_PRICES = 100, 1, 0, 999999

    INGREDIENT_PRICE = 200
    INGREDIENT_TYPE = 'соус'
    INGREDIENT_NAME = 'мазик'

    EXPEXTED_RECEIPT = "(==== Булочка с маком ====)\n" \
                       "= соус мазик =\n" \
                       "= соус мазик =\n" \
                       "(==== Булочка с маком ====)\n" \
                       "\n" \
                       "Price: 600"
