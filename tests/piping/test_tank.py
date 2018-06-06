import pytest
from PipingSystems.storage_tank.tank import Tank


class TestTankLevel:
    def test_tank_level(self):
        tank1 = Tank("tank1", 10)
        assert tank1.level == 10.0

    def test_tank_level_change(self):
        tank1 = Tank()
        tank1.level = 8.0
        assert tank1.level == 8.0

    def test_tank_level_zero(self):
        tank1 = Tank()
        assert tank1.level == 0.0

    def test_tank_level_negative(self):
        tank1 = Tank()
        tank1.level = -1
        assert tank1.level == 0.0

    def test_tank_level_str(self):
        tank1 = Tank()
        with pytest.raises(TypeError) as excinfo:
            tank1.level = "a"
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numeric values only."


class TestTankPressure:
    def test_tank_press(self):
        tank1 = Tank("tank1", 10)
        tank1.static_tank_press = tank1.level
        assert tank1.static_tank_press == 4.335242201711244

    def test_tank_press_change(self):
        tank1 = Tank()
        tank1.level = 8.0
        tank1.static_tank_press = tank1.level
        assert tank1.static_tank_press == 3.4681937613689953

    def test_tank_press_zero(self):
        tank1 = Tank()
        assert tank1.static_tank_press == 0.0

    def test_tank_press_negative(self):
        tank1 = Tank()
        tank1.level = -1
        tank1.static_tank_press = tank1.level
        assert tank1.static_tank_press == 0.0

    def test_tank_press_str(self):
        tank1 = Tank()
        with pytest.raises(TypeError) as excinfo:
            tank1.static_tank_press = "a"
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numeric values only."
