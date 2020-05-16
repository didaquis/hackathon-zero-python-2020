'''
Telegram BOT

Remember install the dependencies: 
	pip install -r exercise_03/requirements.txt

You must create files "bot_token" and "bot_username" and provide real data. Use the tool BothFather of Telegram to create a new bot

Docs: https://python-telegram-bot.org
'''
import logging
from telegram.ext import Updater, CommandHandler

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


def main(): # This is a best practice
	file = open('./exercise_03/bot_token', 'r', encoding='utf-8')
	token = file.read()

	updater = Updater(token, use_context=True)

	print('Bot is running...')

	# Add events handlers:
	updater.dispatcher.add_handler(CommandHandler('start', start_handler)) # Add handler for command '/start'
	updater.dispatcher.add_handler(CommandHandler('eco', echo_handler))
	updater.dispatcher.add_handler(CommandHandler('suma', suma_handler)) # If user writes "/suma 2 3", this bot reponse "El resultado es: 5"

	updater.dispatcher.add_error_handler(error_handler) # Add handler for errors

	updater.start_polling() # Esperamos a pedir notificaciones de telegram
	updater.idle() # Permite que el bot termine de procesar solicitudes si cortamos la ejecución del bot. Es muy recomendable utilizar siempre este método!



def error_handler(update, context):
	'''Send errors to console'''
	logger.warning('Update "%s" caused error "%s"', update.message, context.error)


def start_handler(update, context):
	update.message.reply_text('Hola, soy un bot. Bienvenido!')


def echo_handler(update, context):
	message = update.message.text # get message writed by user
	'''
	update.message contains: 

		{'message_id': 42, 'date': 1589631358, 'chat': {'id': 880840, 'type': 'private', 'username': 'didaquis', 'first_name': 'Dídac', 'last_name': 'García'}, 'text': '/eco testing of course', 'entities': [{'type': 'bot_command', 'offset': 0, 'length': 4}], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 880840, 'first_name': 'Dídac', 'is_bot': False, 'last_name': 'García', 'username': 'didaquis', 'language_code': 'es'}}
	'''
	response = message[5:] # Removing first five characters from the message
	update.message.reply_text(response)


def suma_handler(update, context):
	try:
		sum = int(context.args[0]) + int(context.args[1])
		result = str(sum)
		update.message.reply_text('El resultado es: ' + result)
	except (ValueError):
		update.message.reply_text('Error: please write two numbers')


main()
