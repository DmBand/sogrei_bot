import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from secret import TOKEN
from products import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [cat for cat in categories]
    keyboard.add(*buttons)
    await message.answer(text='Выберите категорию товара, цену которого хотите узнать.\n'
                              'Наличие товара уточняйте по телефону ☎ +375336224802',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='Меню'))
async def get_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [cat for cat in categories]
    keyboard.add(*buttons)
    await message.answer(text='Выберите категорию товара, цену которого хотите узнать.\n'
                              'Наличие товара уточняйте по телефону ☎ +375336224802',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='Гипсокартон'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['🔥 Огнеупорный', '💧 Влагостойкий', '✨ Обычный', 'Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔥 Огнеупорный'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    for dry in DRYWALL['Огнеупорный']:
        answer += f'🔸 {dry}: {"%.2f" % DRYWALL["Огнеупорный"][dry]} руб.\n'
    keyboard.add('💧 Влагостойкий', '✨ Обычный', 'Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='💧 Влагостойкий'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    for dry in DRYWALL['Влагостойкий']:
        answer += f'🔸 {dry}: {"%.2f" % DRYWALL["Влагостойкий"][dry]} руб.\n'
    keyboard.add('🔥 Огнеупорный', '✨ Обычный', 'Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='✨ Обычный'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    for dry in DRYWALL['Обычный']:
        answer += f'🔸 {dry}: {"%.2f" % DRYWALL["Обычный"][dry]} руб.\n'
    keyboard.add('🔥 Огнеупорный', '💧 Влагостойкий', 'Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Клей'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 мешок: 💵\n\n'
    for glu in GLUES:
        answer += f'🔸 {glu}: {"%.2f" % GLUES[glu]} руб.\n'
    keyboard.add('Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Пенопласт'))
async def get_ppt_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1м3: 💵\n\n'
    for ppt in PPT_PRICES:
        answer += f'🔸 {ppt}: {"%.2f" % PPT_PRICES[ppt]} руб.\n'
    keyboard.add('Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Сетка штукатурная'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1м2: 💵\n\n'
    for mesh in FIBERGLASS_MESH:
        answer += f'🔸 {mesh}: {"%.2f" % FIBERGLASS_MESH[mesh]} руб.\n'
    keyboard.add('Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='OSB-плиты влагостойкие'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист: 💵\n\n'
    for osb in OSB_PLATE:
        answer += f'🔸 {osb}: {"%.2f" % OSB_PLATE[osb]} руб.\n'
    keyboard.add('Меню')
    await message.answer(text=answer, reply_markup=keyboard)


# @dp.message_handler(Text(equals='Экструзия'))
# async def get_extrusion(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     answer = '💵 Цена за 1 лист (1180*580мм): 💵\n\n'
#     for ext in EXTRUSION_PRICES:
#         answer += f'🔸 {ext}: {"%.2f" % EXTRUSION_PRICES[ext]} руб.\n'
#     keyboard.add('Меню')
#     await message.answer(text=answer, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
