from unittest import TestCase

from Calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        self.cal = Calc()

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_getsumsum(self):
        self.assertEqual(6, self.cal.get_sumsum(1, 2, 3))

