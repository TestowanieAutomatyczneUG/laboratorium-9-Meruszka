from src.CarImpl import *
from src.Car import *
from unittest.mock import *
from unittest import TestCase

class TestCarImpl(TestCase):
    def test_needsFuel_True(self):
        auto = Car()
        auto.needsFuel = Mock(name="needsFuel")
        auto.needsFuel.return_value = True
        carImpl = CarImpl(auto)
        self.assertEqual("Git", carImpl.fuel_check())
    def test_needsFuel_False(self):
        auto = Car()
        auto.needsFuel = Mock(name="needsFuel")
        auto.needsFuel.return_value = False
        carImpl = CarImpl(auto)
        self.assertEqual("Musisz dolać", carImpl.fuel_check())
    def test_temp_low(self):
        auto = Car()
        auto.getEngineTemperature = Mock(name="getEngineTemperature")
        auto.getEngineTemperature.return_value = 50
        carImpl = CarImpl(auto)
        self.assertEqual("Za mała temperatura", carImpl.tempterature_check())
    def test_temp_nice(self):
        auto = Car()
        auto.getEngineTemperature = Mock(name="getEngineTemperature")
        auto.getEngineTemperature.return_value = 2040
        carImpl = CarImpl(auto)
        self.assertEqual("Wystarczająca temperatura", carImpl.tempterature_check())
    def test_destination_set(self):
        auto = Car()
        auto.driveTo = Mock(name="driveTo")
        auto.driveTo.return_value = "Giżycko"
        carImpl = CarImpl(auto)
        self.assertEqual("Azymut na Giżycko", carImpl.destination_check())
    def test_destination_not_set(self):
        auto = Car()
        auto.driveTo = Mock(name="driveTo")
        auto.driveTo.return_value = None
        carImpl = CarImpl(auto)
        self.assertEqual("Nie ma celu", carImpl.destination_check())