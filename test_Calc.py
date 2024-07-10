from unittest import TestCase

from Calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        self.cal = Calc()

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_getZegop(self):
        tests = [
            {"expected": 1, "num": 1},
            {"expected": 1, "num": -1},
            {"expected": 4, "num": 2},
            {"expected": 16, "num": -4},
            {"expected": 16, "num": -4},
            {"expected": 100, "num": 10},
        ]
        for test in tests:
            with self.subTest(f"getZegop({test["num"]})"):
                self.assertEqual(self.cal.getZegop(test["num"]), test["expected"])
