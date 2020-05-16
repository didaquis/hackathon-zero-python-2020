'''
Execute test with the command:
	python3 -m unittest exercise_02/test/test_*.py
'''

import unittest

from exercise_02.Cat import Cat

class TestCat(unittest.TestCase):

	def test_cat_should_be_callable(self):
		self.assertTrue(callable(Cat), 'Should be callable')

	def test_if_Cat_class_returns_name_of_cat(self):
		name_of_cat = 'Smurf'
		myCat = Cat(name_of_cat)
		self.assertEqual(myCat.getName(), name_of_cat ,'Should return the name of cat')

	def test_if_cat_can_emit_some_sound(self):
		name_of_cat = 'Fido'
		myCat = Cat(name_of_cat)
		self.assertEqual(myCat.talk(), 'miau' ,'Should return: miau')


if __name__ == '__main__':
	unittest.main()