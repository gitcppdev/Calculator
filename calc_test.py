from unittest import TestCase

from calc import sum, sub, mul, div


class TestCalc(TestCase):

    def test_sum_11(self):
        self.assertEqual(sum(1,1), 2)

    def test_sub_11(self):
        self.assertEqual(sub(1,1), 0)

    def test_mul_11(self):
        self.assertEqual(mul(1,1), 1)

    def test_div_11(self):
        self.assertEqual(div(1,1), 1)

    def test_sum_12(self):
        self.assertEqual(sum(1,2), 3)

    def test_sub12(self):
        self.assertEqual(sub(1,2), -1)

    def test_mul12(self):
        self.assertEqual(mul(1,2), 2)

    def test_div12(self):
        self.assertEqual(div(1,2), 0.5)

