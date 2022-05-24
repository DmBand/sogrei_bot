import json
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from secret import TOKEN
from ppt_price_for_one_calculator import get_price_for_one

CATEGORIES = [
    'Гипсокартон',
    'Дюбеля для теплоизоляции',
    'Пенопласт',
    'Профиль',
    'Сетка штукатурная',
    'Сталь',
    'Сухие смеси',
    'OSB-плиты влагостойкие',
]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [cat for cat in CATEGORIES]
    keyboard.add(*buttons)
    await message.answer(text='Выберите категорию товара, цену которого хотите узнать.\n'
                              'Наличие товара уточняйте по телефону ☎ +375336224802',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='✳ Меню'))
async def get_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [cat for cat in CATEGORIES]
    keyboard.add(*buttons)
    await message.answer(text='Выберите категорию товара, цену которого хотите узнать.\n'
                              'Наличие товара уточняйте по телефону ☎ +375336224802',
                         reply_markup=keyboard)


@dp.message_handler(Text(equals='Гипсокартон'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['🔥 Огнеупорный', '💧 Влагостойкий', '✨ Обычный', '✳ Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔥 Огнеупорный'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DRYWALL')
    for dry in data['Огнеупорный']:
        answer += f'🔸 {dry}: {"%.2f" % data["Огнеупорный"][dry]} руб.\n'
    keyboard.add('💧 Влагостойкий', '✨ Обычный', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='💧 Влагостойкий'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DRYWALL')
    for dry in data['Влагостойкий']:
        answer += f'🔸 {dry}: {"%.2f" % data["Влагостойкий"][dry]} руб.\n'
    keyboard.add('🔥 Огнеупорный', '✨ Обычный', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='✨ Обычный'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 лист 1200*2500мм (3м2): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DRYWALL')
    for dry in data['Обычный']:
        answer += f'🔸 {dry}: {"%.2f" % data["Обычный"][dry]} руб.\n'
    keyboard.add('🔥 Огнеупорный', '💧 Влагостойкий', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Дюбеля для теплоизоляции'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['⚒ Стальной гвоздь', '🔨 Пластиковый гвоздь', '✳ Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='⚒ Стальной гвоздь'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1шт: 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DOWEl')
    for dow in data['Стальной гвоздь']:
        answer += f'🔸 {dow}: {"%.2f" % data["Стальной гвоздь"][dow]} руб.\n'
    keyboard.add('🔨 Пластиковый гвоздь', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔨 Пластиковый гвоздь'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1шт: 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DOWEl')
    for dow in data['Пластиковый гвоздь']:
        answer += f'🔸 {dow}: {"%.2f" % data["Пластиковый гвоздь"][dow]} руб.\n'
    keyboard.add('⚒ Стальной гвоздь', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Пенопласт'))
async def get_ppt_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '👇 Какую цену хотите узнать?'
    keyboard.add('📦 Цена за 1м3', '📃 Цена за 1 лист', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='📦 Цена за 1м3'))
async def get_ppt_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1м3: 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('PPT_PRICE_PER_CUBIC_METER')
        for ppt in data:
            answer += f'🔸 {ppt}: {"%.2f" % data[ppt]} руб.\n'
    keyboard.add('📃 Цена за 1 лист', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='📃 Цена за 1 лист'))
async def get_ppt_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '📏 Размер листа: 1000*500мм:\n'
    answer += f'\nПлотность: 10-A\n\n'
    data = get_price_for_one()
    for p in data['ППТ-10-А']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-10-А']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 15-A\n\n'
    for p in data['ППТ-15-А']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-15-А']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 15-Б\n\n'
    for p in data['ППТ-15-Б']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-15-Б']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 20-А\n\n'
    for p in data['ППТ-20-А']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-20-А']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 25-А\n\n'
    for p in data['ППТ-25-А']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-25-А']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 25-Б\n\n'
    for p in data['ППТ-25-Б']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-25-Б']['1000*500мм'][p]} руб.\n"
    answer += f'\nПлотность: 35-A\n\n'
    for p in data['ППТ-35-А']['1000*500мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-35-А']['1000*500мм'][p]} руб.\n"

    answer += '\n📏 Размер листа: 1000x1000мм:\n'
    answer += f'\nПлотность: 10-A\n\n'
    for p in data['ППТ-10-А']['1000*1000мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-10-А']['1000*1000мм'][p]} руб.\n"
    answer += f'\nПлотность: 15-A\n\n'
    for p in data['ППТ-15-А']['1000*1000мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-15-А']['1000*1000мм'][p]} руб.\n"
    answer += f'\nПлотность: 15-Б\n\n'
    for p in data['ППТ-20-А']['1000*1000мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-20-А']['1000*1000мм'][p]} руб.\n"
    answer += f'\nПлотность: 25-А\n\n'
    for p in data['ППТ-25-А']['1000*1000мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-25-А']['1000*1000мм'][p]} руб.\n"
    answer += f'\nПлотность: 35-A\n\n'
    for p in data['ППТ-35-А']['1000*1000мм']:
        answer += f"{p}: {'%.2f' % data['ППТ-35-А']['1000*1000мм'][p]} руб.\n"

    keyboard.add('📦 Цена за 1м3', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Профиль'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена 1шт (3м): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('PROFILE')
    for pr in data:
        answer += f'🔸 {pr}: {"%.2f" % data[pr]} руб.\n'
    keyboard.add('✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Сетка штукатурная'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1м2: 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('FIBERGLASS_MESH')
    for mesh in data:
        answer += f'🔸 {mesh}: {"%.2f" % data[mesh]} руб.\n'
    keyboard.add('✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Сталь'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['🔺 Арматура', '🔹 Трубы профильные', '🔻 Уголок стальной', '✳ Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔺 Арматура'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 прут: 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('STEEL')
    for st in data['Арматура']:
        answer += f'🔸 {st}: {"%.2f" % data["Арматура"][st]} руб.\n'
    keyboard.add('🔹 Трубы профильные', '🔻 Уголок стальной', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔹 Трубы профильные'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 трубу (6м): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('STEEL')
    for st in data['Трубы профильные']:
        answer += f'🔸 {st}: {"%.2f" % data["Трубы профильные"][st]} руб.\n'
    keyboard.add('🔺 Арматура', '🔻 Уголок стальной', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='🔻 Уголок стальной'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1 трубу (6м): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('STEEL')
    for st in data['Уголок стальной']:
        answer += f'🔸 {st}: {"%.2f" % data["Уголок стальной"][st]} руб.\n'
    keyboard.add('🔺 Арматура', '🔹 Трубы профильные', '✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='Сухие смеси'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['Гидроизоляция', 'Клей', 'Кладочные составы', 'Короед',
            'Корник', 'Цемент', 'Шпатлевка', 'Штукатурка', '✳ Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(text=answer, reply_markup=keyboard)


@dp.message_handler(Text(equals='OSB-плиты влагостойкие'))
async def get_extrusion(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '💵 Цена за 1шт (6м): 💵\n\n'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('OSB_PLATE')
    for osb in data:
        answer += f'🔸 {osb}: {"%.2f" % data[osb]} руб.\n'
    keyboard.add('✳ Меню')
    await message.answer(text=answer, reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
