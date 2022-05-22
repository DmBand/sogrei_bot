import telebot
from telebot import types

from secret import TOKEN

bot = telebot.TeleBot(TOKEN)

categories = [
    "пенопласт",
    "экструзия",
    "минеральная вата",
    "кровельный материал",
    "мембраны / пленки",
    "сухие смеси",
    "краски",
    "электрика"
]

PPT_TYPES = ["ППТ10", "ППТ15", "ППТ20", "ППТ25", "ППТ35"]
EXTRUSION_TYPES = ["Истплекс", "Технониколь"]
MINERAL_WOOL = ["Неман", "Профитеп"]
ROOFING_MATERIALS = ["1", "2"]
MEMBRANES = ["Тип А", "Тип В"]
DRY_MIXES = ["цемент", "клей", "штукатурка", "шпатлевка"]
CEMENT = ["Д0", "Д20"]
GLUES = ["Для плитки", "Для блоков"]
STUCCO = ["Илмакс", "Тайфун"]
PUTTY = ["Илмакс", "Тайфун"]
DYE = ["Кондор", "Капрал"]
ELECTRIC = ["Лампочки", "Розетки", "Выключатели"]


def menu_btn():
    return types.KeyboardButton('Меню')


@bot.message_handler(commands=['старт', 'меню'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [types.KeyboardButton(cat.title()) for cat in categories]
    # Добавляем две кнопки
    markup.add(*btns)
    bot.send_message(message.chat.id, text='Выберите категорию товара, цену которого хотите узнать',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text.strip().lower() == 'пенопласт':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(ppt) for ppt in PPT_TYPES]
        markup.add(menu_btn(), *btns)
    elif message.text.strip().lower() == 'экструзия':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(ext) for ext in EXTRUSION_TYPES]
        markup.add(*btns)
    elif message.text.strip().lower() == 'минеральная вата':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(min_w) for min_w in MINERAL_WOOL]
        markup.add(*btns)
    elif message.text.strip().lower() == 'кровельный материал':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(roof) for roof in ROOFING_MATERIALS]
        markup.add(*btns)
    elif message.text.strip().lower() == 'мембраны / пленки':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(mem) for mem in MEMBRANES]
        markup.add(*btns)
    elif message.text.strip().lower() == 'сухие смеси':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(mix) for mix in DRY_MIXES]
        markup.add(*btns)
    elif message.text.strip().lower() == 'краски':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(dye) for dye in DYE]
        markup.add(*btns)
    elif message.text.strip().lower() == 'электрика':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(el) for el in ELECTRIC]
        markup.add(*btns)
    else:
        answer = 'Сделайте выбор'
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer, reply_markup=markup)


# Запускаем бота
bot.polling(none_stop=True, interval=0)

bot.infinity_polling()
