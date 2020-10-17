import telebot
from telebot import types


bot = telebot.TeleBot('*******')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('информация', 'связь')
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('да, давай пообщаемся')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в мой бот!\nМеня зовут Александра.\nЧем могу помочь?',reply_markup=keyboard1)






@bot.message_handler(commands=['insta'])
def instagram(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти в Инстаграм", url="https://www.instagram.com/sparkling_acidity/"))
	bot.send_message(message.chat.id, "В Инстаграме у меня такой же ник, как и в телеге @sparkling_acidity.\nМожешь просто нажать на кнопку ниже и сразу попадешь в мой профиль", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['vk'])
def vk(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton("Перейти на мою страницу ВKонтакте", url="https://vk.com/inspiredbydream"))
	bot.send_message(message.chat.id, "ВKонтакте я отвечаю только на сообщения по работе и учебе, просьба лищний раз не беспокоить.\n"
                                      "По всем вопросам лучше писать в телеграм @sparkling_acidity или на эмейл V-Sash@mail.ru\n", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'информация':
        bot.send_message(message.chat.id, 'Я путешественик и начинающий программист. Это, пожалуй, основное, что стоит знать.\n'
                                          'Но можем пообщаться, хочешь?',reply_markup=keyboard2)
    elif message.text.lower() == 'связь' or 'да, давай пообщаемся':
        bot.send_message(message.chat.id, 'Мой телеграм @sparkling_acidity\n'
                                          'E-mail: V-Sash@mail.ru\n'
                                          'Инстаграм: /insta\n'
                                          'ВК: /vk')







bot.polling(none_stop=True, interval=0)