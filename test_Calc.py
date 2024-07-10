from unittest import TestCase

from Calc import Calc


class TestCalc(TestCase):
    def setUp(self):
        self.cal = Calc()

    def test_case1(self):
        self.assertEqual(1, 1)

    def test_minus1(self):
        calc = Calc()
        expect = 1

        actual = calc.getMinus(3, 2)

        self.assertEqual(actual, expect)

    def test_minus2(self):
        calc = Calc()
        expect = -3

        actual = calc.getMinus(0, 3)

        self.assertEqual(actual, expect)