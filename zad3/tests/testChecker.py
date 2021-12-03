from src.Checker import Checker
from src.main import Env
from unittest.mock import *
from unittest import TestCase
from datetime import datetime


class TestChecker(TestCase):
    @patch.object(Env, 'getTime')
    def test_reminder_before_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2001, 1, 1, 12, 0, 5, 5)
        checker = Checker()
        checker.resetWave()
        checker.reminder()
        self.assertEqual(False, checker.was_played())

    @patch.object(Env, 'getTime')
    def test_reminder_after_17(self, mock_method) -> None:
        mock_method.return_value = datetime(2021, 1, 1, 17, 0, 0, 1)
        checker = Checker()
        checker.resetWave()
        checker.reminder()
        self.assertEqual(True, checker.was_played())