from src.Car import *
from unittest.mock import *
from unittest import TestCase

class test_Car_public_interface(TestCase):
    def setUp(self):
        def fuel(ilosc):
            if ilosc > 0:
                return True
            return False
        #prepare mock
        self.test_object = Car()
        self.test_object.needsFuel = Mock(name = 'needsFuel')
        self.test_object.needsFuel = fuel

    def test_needsFuel_5(self):
        self.assertEqual(True, self.test_object.needsFuel(5), 'return value from public_method incorrect')
    
    def test_needsFuel_10(self):
        self.assertEqual(True, self.test_object.needsFuel(10), 'return value from public_method incorrect')
    
    def test_needsFuel_negative_1(self):
        self.assertEqual(False, self.test_object.needsFuel(-1), 'return value from public_method incorrect')

    def test_needsFuel_0(self):
        self.assertEqual(False, self.test_object.needsFuel(0), 'return value from public_method incorrect')

    def test_needsFuel_negative_100(self):
        self.assertEqual(False, self.test_object.needsFuel(-100), 'return value from public_method incorrect')

    def test_needsFuel_100(self):
        self.assertEqual(True, self.test_object.needsFuel(100), 'return value from public_method incorrect')
    
    def test_needsFuel_47568374687(self):
        self.assertEqual(True, self.test_object.needsFuel(4356823758), 'return value from public_method incorrect')
