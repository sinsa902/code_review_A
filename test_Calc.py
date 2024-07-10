from unittest import TestCase

from Calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        self.cal = Calc()

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_get_sum(self):
        self.assertEqual(3, self.cal.get_sum(1,2))
        self.assertEqual(6, self.cal.get_sum(3, 3))