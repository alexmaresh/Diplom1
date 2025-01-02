from praktikum.bun import Bun


class TestBun:
    def test_bun_add_name_success(self):
        """Проверяем метод get_name()."""
        bun = Bun("Сладкая", 12.0)
        assert bun.get_name() == "Сладкая"

    def test_bun_add_price_success(self):
        """Проверяем метод get_price()."""
        bun = Bun("С кунжутом", 11.5)
        assert bun.get_price() == 11.5

    def test_bun_invalid_price_fail(self):
        """Проверяем, что не происходит ошибка при инициализации с нулевой ценой."""
        bun = Bun("Plain", 0.0)
        assert bun.get_price() == 0.0

    def test_bun_string_name(self):
        """Проверяем, что имя булочки корректно сохраняется как строка."""
        bun = Bun("Круглая булка", 3.0)
        assert isinstance(bun.get_name(), str)

    def test_bun_float_price(self):
        """Проверяем, что цена булочки корректно сохраняется как float."""
        bun = Bun("Квадратная булка", 1.75)
        assert isinstance(bun.get_price(), float)
