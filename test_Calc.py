from unittest import TestCase

from Calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        cal = Calc()

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_getgop(self, a, b)
        self.assertEqual(8, cal.getGop(2, 4))
