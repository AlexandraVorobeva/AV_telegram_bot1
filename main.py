import telebot
from telebot import types


bot = telebot.TeleBot('891829442:AAF17IVzOFGrEG5Pc3tN9vURdgcCMmVBiwI')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('информация', 'связь')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('давай общаться')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в мой бот!\nМеня зовут Александра.\nЧем могу помочь?',reply_markup=keyboard1)






@bot.message_handler(commands=['insta'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/sparkling_acidity/"))
	bot.send_message(message.chat.id, "В Инстаграме у меня такой же ник, как и в телеге @sparkling_acidity.\nМожешь просто нажать на кнопку ниже и сразу попадешь в мой профиль", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['git'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на мой Git Hub", url="https://github.com/SparklingAcidity"))
	bot.send_message(message.chat.id, "Здесь можно посмотреть мои лучшие готовые проекты.", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'информация':
        bot.send_message(message.chat.id, 'Я начинаюший веб разработчик на Питоне.\n'
                                          'Ты можешь выбрать любой удобный тебе способ связи',reply_markup=keyboard2)
    elif message.text.lower() == 'связь' or 'давай общаться':
        bot.send_message(message.chat.id, 'Мой телеграм @sparkling_acidity\n'
                                          'E-mail: V-Sash@mail.ru\n'
                                          'Инстаграм: /insta\n'
                                          'Git Hub: /git')







bot.polling(none_stop=True, interval=0)