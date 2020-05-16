import unittest

from exercise_04.PasswordGenerator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):

	def test_should_be_callable(self):
		self.assertTrue(callable(PasswordGenerator), 'Should be callable')

	def test_should_return_a_string(self):
		generator = PasswordGenerator()
		password = generator.new_password()
		self.assertGreaterEqual(len(password), 8, 'Should have at least 8 characters')

if __name__ == '__main__':
	unittest.main()