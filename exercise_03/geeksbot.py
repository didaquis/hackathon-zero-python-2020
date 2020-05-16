'''
Telegram BOT

Remember install the dependencies: 
	pip install -r exercise_03/requirements.txt
'''

from telegram.ext import Updater

def main(): # This is a best practice
	updater = Updater(token = '')
