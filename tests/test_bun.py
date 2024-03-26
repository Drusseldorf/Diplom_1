from praktikum_dir.bun import Bun
from data.data_values import Values


class TestBun:

    def test_get_name(self):
        bun = Bun(Values.BUN_NAME_1, 100)
        assert bun.get_name() == Values.BUN_NAME_1

    def test_get_price(self):
        bun = Bun(Values.BUN_NAME_1, 100)
        assert bun.get_price() == 100
