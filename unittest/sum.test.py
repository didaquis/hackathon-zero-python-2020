import unittest

from sum import sum

class TestSum(unittest.TestCase):

	def test_sum_should_be_callable(self):
		self.assertTrue(callable(sum), "Should be callable")

	def test_sum(self):
		self.assertEqual(sum(1,2), 3, "Should be 3")

if __name__ == '__main__':
	unittest.main()