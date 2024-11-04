import telebot
from telebot import types
import threading
import signal
import sys

bot = telebot.TeleBot('YourToken')

running = False

def run_bot():
    while running:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(f"Error: {e}")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global running
    if not running:
        bot.send_message(message.chat.id, "Bot restarted.")
        running = True
        threading.Thread(target=run_bot).start()
    else:
        keyboard = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='YourName1', callback_data='firstcallback')
        key_second = types.InlineKeyboardButton(text='YourName2', callback_data='secondcallback')
        key_third = types.InlineKeyboardButton(text='YourName3', callback_data='thirdcallback')
        key_fourth = types.InlineKeyboardButton(text='YourName4', callback_data='fourthcallback')
        key_fifth = types.InlineKeyboardButton(text='YourName5', callback_data='fifthcallback')
        key_sixth = types.InlineKeyboardButton(text='YourName6', callback_data='sixthcallback')
        keyboard.add(key_first, key_second, key_third, key_fourth, key_fifth, key_sixth)

        question = 'Your question:\n'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global running
    bot.send_message(message.chat.id, "The bot is stopped. Type /start to activate the bot again.")
    running = False


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()


    bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == "secondcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName2\nYourlink2 : https://www.google.com', reply_markup=keyboard)
    elif call.data == "firstcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName1\nYourlink1 : https://www.google.com', reply_markup=keyboard)
    elif call.data == "thirdcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName3\nYourlink3 : https://www.google.com', reply_markup=keyboard)
    elif call.data == "fourthcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName4\nYourlink4 : https://www.google.com', reply_markup=keyboard)
    elif call.data == "fifthcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName5\nYourlink5 : https://www.google.com', reply_markup=keyboard)
    elif call.data == "sixthcallback":
        key_back = types.InlineKeyboardButton(text='Back', callback_data='back')
        keyboard.add(key_back)
        bot.send_message(call.message.chat.id, 'YourName6\nYourlink6 : https://www.google.com', reply_markup=keyboard)

    elif call.data == "back":

        key_first = types.InlineKeyboardButton(text='YourName1', callback_data='firstcallback')
        key_second = types.InlineKeyboardButton(text='YourName2', callback_data='secondcallback')
        key_third = types.InlineKeyboardButton(text='YourName3', callback_data='thirdcallback')
        key_fourth = types.InlineKeyboardButton(text='YourName4', callback_data='fourthcallback')
        key_fifth = types.InlineKeyboardButton(text='YourName5', callback_data='fifthcallback')
        key_sixth = types.InlineKeyboardButton(text='YourName6', callback_data='sixthcallback')
        keyboard.add(key_first, key_second, key_third, key_fourth, key_fifth, key_sixth)
        question = 'YourQuestion:\n'
        bot.send_message(call.message.chat.id, question, reply_markup=keyboard)


    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id)



def signal_handler(sig, frame):
    global running
    running = False
    print("Stop bot...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    running = True
    threading.Thread(target=run_bot).start()
