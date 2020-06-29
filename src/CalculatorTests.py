import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('src/addition.csv').data
        for role in test_data:
            self.assertEqual(self.calculator.add(row['Value 1']), ((row['Value 2']), int(row['Result'])))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('src/subtraction.csv').data
        for role in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1']), ((row['Value 2']), int(row['Result'])))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/multiplication.csv').data
        for role in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1']), ((row['Value 2']), int(row['Result'])))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('src/division.csv').data
        for role in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1']), ((row['Value 2']), int(row['Result'])))
            self.assertEqual(self.calculator.result, int(row['Result']))

                    if __name__ == '__main__':
    unittest.main()