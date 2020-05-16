import unittest

from exercise_04.PasswordGenerator import PasswordGenerator

class TestSum(unittest.TestCase):

	def test_PasswordGenerator_should_be_callable(self):
		self.assertTrue(callable(PasswordGenerator), 'Should be callable')



if __name__ == '__main__':
	unittest.main()