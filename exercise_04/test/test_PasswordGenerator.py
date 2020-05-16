import unittest
import re

from exercise_04.PasswordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

	def test_should_be_callable(self):
		self.assertTrue(callable(PasswordGenerator), 'Should be callable')

	def test_should_return_a_string_enough_length(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(isinstance(password, str), 'Should be a string')
		self.assertGreaterEqual(len(password), 8, 'Should have at least 8 characters')

	def test_should_contain_at_least_one_letter_lowercase(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(re.search('[a-z]', password), 'Should contain a letter in lowercase')

	def test_should_contain_at_least_one_letter_uppercasee(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(re.search('[A-Z]', password), 'Should contain a letter in uppercase')

	def test_should_contain_at_least_one_number(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(re.search('[0-9]', password), 'Should contain a number')

if __name__ == '__main__':
	unittest.main()