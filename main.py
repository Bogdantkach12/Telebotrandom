
# Підключаємо модуля для створення ботів
import telebot
import random
# ідентифікатори
# message.from_user.first_name - отримуємо перше ім'я користувача з повідомлення до бота
# message.from_user.username - отримуємо псевдонім користувача з повідомлення до бота
# message.from_user.last_name - отримуємо друге ім'я (прізвище) користувача з повідомлення до бота
# message.chat.id - отримує id чата відправника
# message.text - 

# Підключаю бота до телеграму
bot = telebot.TeleBot('5660951250:AAGP1q1REgAG2ViX4TNM4Q_lntqf61mtdpA')
# задаємо обробку повідомлень
@bot.message_handler(commands=['start'])
# Фукнція що обробляє команду "/start"
def bot_start(message):
    # бот відправляє повідомлення користувачу, що відправив команду "/start"
    bot.send_message(message.chat.id, "Hello, User!", reply_markup= keyboard_play)
    bot.register_next_step_handler(message, all_messages)
# Створюємо кнопку Play
button_play = telebot.types.KeyboardButton("Play")
# Cстворюємо клавіатуру
keyboard_play = telebot.types.ReplyKeyboardMarkup()
# Додаємо кнопку button_play до клавіатури
keyboard_play.add(button_play)

def all_messages(message):
    if message.text.lower() == "play":
        number = random.randint(1, 4)
        button1 = telebot.types.KeyboardButton("1")
        button2 = telebot.types.KeyboardButton("2")
        button3 = telebot.types.KeyboardButton("3")
        button4 = telebot.types.KeyboardButton("4")
        keyboard_number = telebot.types.ReplyKeyboardMarkup()
        keyboard_number.add(button1, button2)
        keyboard_number.add(button3, button4)
        bot.send_message(message.chat.id, "Starting the game, choose one from options!", reply_markup = keyboard_number)
        bot.register_next_step_handler(message, win_over, number)
    if message.text.lower() == "/hi":
        bot.send_message(message.chat.id, f"Nice to meet you! {message.from_user.username}!")
    #
    bot.register_next_step_handler(message, all_messages)
# функція що перевіряє чи вгадали ми число   
def win_over(message, number):
    # Умова що перевіряє чи вгадали ми число
    if message.text == str(number):
        bot.send_message(message.chat.id, f"Congratulations, {message.from_user.first_name}! You guessed the number.", reply_markup= keyboard_play)
    else:
        bot.send_message(message.chat.id, f"Sorry, {message.from_user.first_name}! You didn`t guess the number.", reply_markup= keyboard_play)
# опитує команди
bot.polling()
