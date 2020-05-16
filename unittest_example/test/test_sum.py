'''
For run all test execute this ("unittest_example" is the name of target folder): 
	python3 -m unittest discover unittest_example/

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

	def test_sum(self):
		self.assertEqual(sum(1,2), 3, "Should be 3")

if __name__ == '__main__':
	unittest.main()