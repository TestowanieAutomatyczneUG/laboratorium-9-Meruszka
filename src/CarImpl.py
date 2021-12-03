from src.Car import Car

class CarImpl():
    def __init__(self, car: Car):
        self._car = car
    def fuel_check(self):
        if self._car.needsFuel():
            return "Git"
        return "Musisz dolać"
    def tempterature_check(self):
        stp = self._car.getEngineTemperature()
        if stp < 100:
            return "Za mała temperatura"
        return "Wystarczająca temperatura"
    def destination_check(self):
        des = self._car.driveTo()
        if des is not None:
            return "Azymut na " + str(des)
        return "Nie ma celu"