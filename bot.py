import telebot
from telebot import types

from secret import TOKEN
from products import *

bot = telebot.TeleBot(TOKEN)


def menu_btn():
    return types.KeyboardButton('Меню')


@bot.message_handler(commands=['старт'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [types.KeyboardButton(cat.capitalize()) for cat in categories]
    # Добавляем две кнопки
    markup.add(*btns)
    bot.send_message(message.chat.id, text='Выберите категорию товара, цену которого хотите узнать',
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text.strip().lower() == 'меню':
        return start(message)
    elif message.text.strip().lower() == 'пенопласт':
        answer = 'Цена за м3:\n\n'
        for ppt in PPT_PRICES:
            answer += f'{ppt}: {PPT_PRICES[ppt]} руб.\n'
        markup.add(menu_btn())

    elif message.text.strip().lower() == 'экструзия':
        answer = 'Цена за лист (1180*580мм):\n\n'
        for ext in EXTRUSION_PRICES:
            answer += f'{ext}: {EXTRUSION_PRICES[ext]} руб.\n'
        markup.add(menu_btn())
    # elif message.text.strip().lower() == 'минеральная вата':
    #     answer = 'Выберите тип'
    #     btns = [types.KeyboardButton(min_w) for min_w in MINERAL_WOOL]
    #     markup.add(*btns)
    # elif message.text.strip().lower() == 'кровельный материал':
    #     answer = 'Выберите тип'
    #     btns = [types.KeyboardButton(roof) for roof in ROOFING_MATERIALS]
    #     markup.add(*btns)
    # elif message.text.strip().lower() == 'мембраны / пленки':
    #     answer = 'Выберите тип'
    #     btns = [types.KeyboardButton(mem) for mem in MEMBRANES]
    #     markup.add(*btns)
    # elif message.text.strip().lower() == 'сухие смеси':
    #     answer = 'Выберите тип'
    #     btns = [types.KeyboardButton(mix) for mix in DRY_MIXES]
    #     markup.add(*btns)
    # elif message.text.strip().lower() == 'краски':
    #     answer = 'Выберите тип'
    #     btns = [types.KeyboardButton(dye) for dye in DYE]
    #     markup.add(*btns)
    elif message.text.strip().lower() == 'электрика':
        answer = 'Выберите тип'
        btns = [types.KeyboardButton(el) for el in ELECTRIC]
        markup.add(menu_btn(), *btns)
    else:
        answer = 'Сделайте выбор'
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(chat_id=message.chat.id, text=answer, reply_markup=markup)


# Запускаем бота
bot.polling(none_stop=True, interval=0)

bot.infinity_polling()
