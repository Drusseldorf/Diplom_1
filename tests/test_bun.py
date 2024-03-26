from praktikum_dir.bun import Bun
from data.data_values import Values


class TestBun:

    def test_get_name(self):
        bun = Bun(Values.BUN_NAME, Values.BUN_PRICE)
        assert bun.get_name() == Values.BUN_NAME

    def test_get_price(self):
        bun = Bun(Values.BUN_NAME, Values.BUN_PRICE)
        assert bun.get_price() == Values.BUN_PRICE
