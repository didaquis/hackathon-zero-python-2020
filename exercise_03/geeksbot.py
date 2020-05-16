'''
Telegram BOT

Remember install the dependencies: 
	pip install -r exercise_03/requirements.txt

You must create files "bot_token" and "bot_username" and provide real data. Use the tool BothFather of Telegram to create a new bot

Docs: https://python-telegram-bot.org
'''

from telegram.ext import Updater

def main(): # This is a best practice
	file = open('./exercise_03/bot_token', 'r', encoding='utf-8')
	token = file.read()

	updater = Updater(token, use_context=True)





	updater.start_polling() # Esperamos a pedir notificaciones de telegram
	updater.idle() # Permite que el bot termine de procesar solicitudes si cortamos la ejecución del bot. Es muy recomendable utilizar siempre este método!


main()
