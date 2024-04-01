import pytest

from praktikum_dir.bun import Bun
from data.data_values import Values


class TestBun:

    def test_get_name(self):
        bun = Bun(Values.BUN_NAME, Values.BUN_PRICE)
        assert bun.get_name() == Values.BUN_NAME

    @pytest.mark.parametrize('bun_price', [Values.BUN_PRICES[0],
                                           Values.BUN_PRICES[1],
                                           Values.BUN_PRICES[2],
                                           Values.BUN_PRICES[3]])
    def test_get_price(self, bun_price):
        bun = Bun(Values.BUN_NAME, bun_price)
        assert bun.get_price() == bun_price
