import telebot

token = '5644986743:AAHEAT0zsHB_y-WhpesX9SDsharZfrzUefU'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Поработать')
    item2 = telebot.types.KeyboardButton('Отдохнуть')
    item3 = telebot.types.KeyboardButton('Помыться')
    item4 = telebot.types.KeyboardButton('Сделать уборку')
    item5 = telebot.types.KeyboardButton('Поучиться')

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Привет, чем хочешь заняться?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'поработать':
        bot.send_message(message.chat.id, 'Если хочешь поработать, ляг поспи и всё пройдёт')
    elif message.text.lower() == 'отдохнуть':
        bot.send_message(message.chat.id, 'Вы посмотрите на него, устал видите-ли')
    elif message.text.lower() == 'помыться':
        bot.send_message(message.chat.id, 'Моются ленивые, остальные чешутся')
    elif message.text.lower() == 'сделать уборку':
        bot.send_message(message.chat.id, 'Да ладно тебе, грязь толщиной до сантиметра-не грязь, а больше, сама отваливается')
    elif message.text.lower() == 'поучиться':
        bot.send_message(message.chat.id, 'Правильно, ученье-свет, а неученье-чуть свет и на работу')