import unittest
import calculator


class TestAddFunctionality(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        result = calculator.calc_add(10, 20)
        self.assertEqual(result, 30)

    def test_add_one_number_one_string_a(self):
        result = calculator.calc_add(10, '20')
        self.assertEqual(result, 30)

    def test_add_one_number_one_string_b(self):
        with self.assertRaises(TypeError):
            result = calculator.calc_add(10, '20') #its done here itself
            self.assertEqual(result, 30)

