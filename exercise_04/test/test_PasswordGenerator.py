import unittest
import re

from exercise_04.PasswordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

	def test_should_be_callable(self):
		self.assertTrue(callable(PasswordGenerator), 'Should be callable')

	def test_should_return_a_string(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(isinstance(password, str), 'Should be a string')

	def test_should_return_a_string_enough_length(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		expected_length = 32
		self.assertGreaterEqual(len(password), expected_length, 'Should have at least {} characters'.format(expected_length))

	def test_should_contain_at_least_one_letter_lowercase(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(re.search('[a-z]', password), 'Should contain a letter in lowercase')

	def test_should_contain_at_least_one_number(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertTrue(re.search('[0-9]', password), 'Should contain a number')

	def test_should_return_different_token_on_every_call(self):
		generator = PasswordGenerator()
		list_of_tokens = []
		
		number_of_tokens_to_generate = 999
		number_of_expected_tokens = number_of_tokens_to_generate
		while number_of_tokens_to_generate > 0:
			password = generator.new_password()

			if password not in list_of_tokens:
				list_of_tokens.append(password)

			number_of_tokens_to_generate -= 1
		
		self.assertEqual(len(list_of_tokens), number_of_expected_tokens, 'Should generate 999 unique tokens')

if __name__ == '__main__':
	unittest.main()