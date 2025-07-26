import unittest
from calculator_v2 import Calculator


class TestCalculator_v2(unittest.TestCase):

    def test_add_functionality(self):
        calc1=Calculator(10,-20)
        result=calc1.calc_add()
        self.assertEqual(result,-10)
