'''
For run all test execute this ("unittest_example" is the name of target folder): 
	python3 -m unittest discover unittest_example/
	python3 -m unittest discover -s unittest_example

All test must be in directory called "test".

Ensure you have a "__init__.py" file on that directory.

All files must be name with this pattern "test_foo.py".


Other options:
	python3 -m unittest unittest_example/test/*.py
	python3 -m unittest unittest_example/test/test_sum.py
	python3 -m unittest unittest_example/test/test_*.py
'''

import unittest

from unittest_example.sum import sum # from <name_of_file> import <function>

class TestSum(unittest.TestCase):

	def test_sum_should_be_callable(self): # Name of test should be unique
		self.assertTrue(callable(sum), "Should be callable")

	def test_sum_should_return_zero_if_not_receive_integers(self):
		self.assertEqual(sum(), 0, "Should be 0")

	def test_sum_two_integers(self):
		self.assertEqual(sum(1,2), 3, "Should be 3")

	def test_sum_any_number_of_integers(self):
		self.assertEqual(sum(1,2,3,4,2,1), 13, "Should be 13")

	def test_sum_with_float_numbers(self):
		self.assertAlmostEqual(sum(1.1,2.2), 3.30000)

if __name__ == '__main__':
	unittest.main()