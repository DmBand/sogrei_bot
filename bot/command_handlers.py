import json
import math
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from admin import check_permission
from db_manager import DBHandler
from secret import TOKEN
from ppt_price_for_one_calculator import get_price_for_one


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = DBHandler()

CATEGORIES = [
    'Гипсокартон',
    'Дюбеля для теплоизоляции',
    'Краски',
    'Минеральная вата',
    '✨ Пенопласт',
    'Профиль',
    'Сетка штукатурная',
    'Сталь',
    'Сухие смеси',
    'OSB-плиты влагостойкие',
    '📄 Контакты',
    '✅ Рассчитать пенопласт'
]

main_menu = '❗ ВСЕ ЦЕНЫ НА ТОВАР УКАЗАНЫ <b>БЕЗ УЧЕТА СКИДОК</b> ❗\n\n' \
            'Наличие товара уточняйте по телефонам ☎\n' \
            '🔹 +375336224802 <b>(МТС)</b>\n' \
            '🔹 +375447717753 <b>(А1)</b>\n' \
            '🔹 32-12-12 <b>(Городской)</b>\n\n' \
            '<a href="https://www.instagram.com/sogrey_m.grodno/"><b>🌄 Следите за нами в Instagram</b></a>\n\n' \
            '<b>Выберите категорию товара, \n' \
            'цену которого хотите узнать 👇</b>\n'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=[
    'start',
    'старт',
    'menu',
    'Menu'
])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1
    )
    buttons = [cat for cat in CATEGORIES]
    keyboard.add(*buttons)
    await message.answer(
        text=main_menu,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '✳ Меню',
    'Меню',
    'меню'
]))
async def get_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=1
    )
    buttons = [cat for cat in CATEGORIES]
    keyboard.add(*buttons)
    await message.answer(
        text=main_menu,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '📄 Контакты',
    'Контакты',
    'контакты'
]))
async def get_contacts(message: types.Message):
    answer = '<b>✔ ЧПТУП "Согрей-М"\n</b>' \
             'г.Гродно, ул.Соколовского, 20Г\n\n' \
             '<b>🕒 ВРЕМЯ РАБОТЫ:</b>\n\n' \
             '💸 <b>Магазин</b>\n' \
             'понедельник-пятница: <b>08:30 - 19:00</b>\n' \
             'суббота: <b>9:00 - 18:00</b>\n' \
             'воскресенье: <b>9:00 - 17:00</b>\n' \
             '❎ <b>БЕЗ ОБЕДА И ВЫХОДНЫХ</b>\n' \
             '📞 +375336224802 <b>МТС</b>\n' \
             '📞 +375447717753 <b>А1</b>\n' \
             '📞 32-12-12 <b>(Городской)</b>\n\n' \
             '🧰 <b>Отдел продаж</b>\n' \
             'понедельник-пятница: <b>08:00 - 17:00</b>\n' \
             'суббота-воскресенье: <b>выходной</b>\n' \
             '📞 +375297804352 <b>(МТС)</b>\n' \
             '📞 +375291990505 <b>(A1)</b>\n' \
             '📞 32-06-06 <b>(Городской)</b>\n\n' \
             '<a href="https://www.instagram.com/sogrey_m.grodno/"><b>🌄 Мы в Instagram</b></a>\n\n' \
             '<a href="https://goo.gl/maps/JfKL7NW7Bsdo4zVZ8">🌎 <b>МЫ НА КАРТЕ</b> 👈</a>'
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Гипсокартон',
    'гипсокартон'
]))
async def get_drywall(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [
        '🔥 Огнеупорный',
        '💧 Влагостойкий',
        '✨ Обычный',
        '✳ Меню',
    ]
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '🔥 Огнеупорный',
    'Огнеупорный',
    'огнеупорный'
]))
async def get_refactory_drywall(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_drywall('Огнеупорный')
    keyboard.add(
        '💧 Влагостойкий',
        '✨ Обычный',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '💧 Влагостойкий',
    'Влагостойкий',
    'влагостойкий'
]))
async def get_moisture_resistant_drywal(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_drywall('Влагостойкий')
    keyboard.add(
        '🔥 Огнеупорный',
        '✨ Обычный',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '✨ Обычный',
    'Обычный',
    'обычный'
]))
async def get_simple_drywall(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_drywall('Обычный')
    keyboard.add(
        '🔥 Огнеупорный',
        '💧 Влагостойкий',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Дюбеля для теплоизоляции',
    'дюбеля для теплоизоляции'
]))
async def get_dowel(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    btns = [
        '⚒ Стальной гвоздь',
        '🔨 Пластиковый гвоздь',
        '✳ Меню',
    ]
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '⚒ Стальной гвоздь',
    'Стальной гвоздь',
    'стальной гвоздь'
]))
async def get_steel_dowel(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = db.get_dowel('Стальной гвоздь')
    keyboard.add(
        '🔨 Пластиковый гвоздь',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔨 Пластиковый гвоздь',
    'Пластиковый гвоздь',
    'пластиковый гвоздь'
]))
async def get_plastic_dowel(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = db.get_dowel('Пластиковый гвоздь')
    keyboard.add(
        '⚒ Стальной гвоздь',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '⬅ Краски',
    'Краски',
    'краски'
]))
async def get_paints(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [
        '🔻 Тайфун Мастер',
        '🔸 Condor',
        '🔹 Kapral',
        '🔺 Malevanka',
        '▫ Sniezka',
        '✳ Меню',
    ]
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '🔻 Тайфун Мастер',
    'Тайфун Мастер',
    'Тайфун мастер',
    'тайфун Мастер',
    'тайфун мастер'
]))
async def get_paints_taifun(message: types.Message):
    answer = db.get_paints(description='Тайфун Мастер')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔸 Condor',
    'Condor',
    'сondor',
    'Кондор',
    'кондор'
]))
async def get_paints_condor(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '👇 Выберите тип'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('PAINT').get('Condor')
        btns = [b for b in data]
        keyboard.add(*btns, '⬅ Краски', '✳ Меню')
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    'Белые интерьеры',
    'белые интерьеры'
]))
async def get_paints_condor_white_interiors(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Белые интерьеры'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Для потолков',
    'для потолков'
]))
async def get_paints_condor_ceiling(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Для потолков'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Кухни и ванные',
    'кухни и ванные'
]))
async def get_paints_condor_kitchen(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Кухни и ванные'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Латексная',
    'латексная'
]))
async def get_paints_condor_latex(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Латексная'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Фасады',
    'фасады'
]))
async def get_paints_condor_front(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Фасады'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Школы и офисы',
    'школы и офисы'
]))
async def get_paints_condor_schools(message: types.Message):
    answer = db.get_paints(
        description='Condor',
        description2='Школы и офисы'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔹 Kapral',
    'Kapral',
    'kapral',
    'Капрал',
    'капрал'
]))
async def get_paints_kapral(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '👇 Выберите тип'
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('PAINT').get('Kapral')
        btns = [b for b in data]
        keyboard.add(
            *btns,
            '⬅ Краски',
            '✳ Меню',
        )
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    'Интерьерная',
    'интерьерная'
]))
async def get_paints_kapral_interior(message: types.Message):
    answer = db.get_paints(
        description='Kapral',
        description2='Интерьерная'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Моющаяся',
    'моющаяся'
]))
async def get_paints_kapral_washable(message: types.Message):
    answer = db.get_paints(
        description='Kapral',
        description2='Моющаяся'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Супербелая',
    'супербелая'
]))
async def get_paints_kapral_superwhite(message: types.Message):
    answer = db.get_paints(
        description='Kapral',
        description2='Супербелая'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Фасадная',
    'фасадная'
]))
async def get_paints_kapral_front(message: types.Message):
    answer = db.get_paints(
        description='Kapral',
        description2='Фасадная'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔺 Malevanka',
    'Malevanka',
    'malevanka',
    'Малеванка',
    'малеванка'
]))
async def get_paints_malevanka(message: types.Message):
    answer = db.get_paints(description='Malevanka')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '▫ Sniezka',
    'Sniezka',
    'sniezka',
    'Снежка',
    'снежка'
]))
async def get_paints_sniezka(message: types.Message):
    answer = db.get_paints(description='Sniezka')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Минеральная вата',
    'минеральная вата'
]))
async def get_mineral_wool(message: types.Message):
    answer = db.get_mineral_wool()
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '✨ Пенопласт',
    'пенопласт',
    'пенопласт'
]))
async def get_ppt_price(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer = '👇 Какую цену хотите узнать?'
    keyboard.add(
        '📦 Цена за 1м3',
        '📃 Цена за 1 лист',
        '✳ Меню',
        '✅ Рассчитать пенопласт',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '📦 Цена за 1м3',
    'Цена за 1м3',
    'цена за 1м3'
]))
async def get_ppt_price_per_cubic_meter(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_ppt_cubic_meter()
    keyboard.add(
        '📃 Цена за 1 лист',
        '✳ Меню',
        '✅ Рассчитать пенопласт',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '📃 Цена за 1 лист',
    'Цена за 1 лист',
    'цена за 1 лист'
]))
async def get_ppt_price_for_one(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_ppt_one_sheet()
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Профиль',
    'профиль'
]))
async def get_profile(message: types.Message):
    answer = db.get_profile()
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Сетка штукатурная',
    'сетка штукатурная'
]))
async def get_fiberglass_mesh(message: types.Message):
    answer = db.get_fiberglass_mesh()
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Сталь',
    'сталь'
]))
async def get_steel(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ['🔺 Арматура', '🔹 Трубы профильные', '🔻 Уголок стальной', '✳ Меню']
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '🔺 Арматура',
    'Арматура',
    'арматура'
]))
async def get_fittings(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_steel(description='Арматура')
    keyboard.add(
        '🔹 Трубы профильные',
        '🔻 Уголок стальной',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔹 Трубы профильные',
    'Трубы профильные',
    'трубы профильные'
]))
async def get_pipe(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_steel(description='Трубы профильные')
    keyboard.add(
        '🔺 Арматура',
        '🔻 Уголок стальной',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔻 Уголок стальной',
    'Уголок стальной',
    'уголок стальной'
]))
async def get_corner(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    answer = db.get_steel(description='Уголок стальной')
    keyboard.add(
        '🔺 Арматура',
        '🔹 Трубы профильные',
        '✳ Меню',
    )
    await message.answer(
        text=answer,
        reply_markup=keyboard,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '⬅ Сухие смеси',
    'Сухие смеси',
    'сухие смеси'
]))
async def get_dry_mixes(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [
        '💧 Гидроизоляция',
        '🟥 Гипс строительный',
        '🟧 Клеевые составы',
        '🧱 Кладочные составы',
        '🟨 Короед',
        '🟩 Корник',
        '🟫 Самонивелиры',
        '🔴 Стяжки',
        '⚪ Цемент',
        '🟡 Шпатлевка',
        '🟢 Штукатурка',
        '🟣 Шуба',
        '✳ Меню',
    ]
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    '💧 Гидроизоляция',
    'Гидроизоляция',
    'гидроизоляция'
]))
async def get_waterproofing(message: types.Message):
    answer = db.get_dry_mixes(description='Гидроизоляция')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟥 Гипс строительный',
    'Гипс строительный',
    'гипс строительный'
]))
async def get_gypsum(message: types.Message):
    answer = db.get_dry_mixes(description='Гипс строительный')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟧 Клеевые составы',
    'Клеевые составы',
    'клеевые составы'
]))
async def get_glues(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=2
    )
    with open('products.json', 'r', encoding='utf8') as f:
        data = json.load(f).get('DRY_MIXES')
    btn = [k for k in data['Клеевые составы'].keys()]
    btns = [
        *btn,
        '⬅ Сухие смеси',
        '✳ Меню',
    ]
    answer = '👇 Выберите тип'
    keyboard.add(*btns)
    await message.answer(
        text=answer,
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals=[
    'Гипсовые',
    'гипсовые'
]))
async def get_gypsum_glue(message: types.Message):
    answer = db.get_dry_mixes(
        description='Клеевые составы',
        description2='Гипсовые'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Для блоков',
    'для блоков'
]))
async def get_glue_for_blocks(message: types.Message):
    answer = db.get_dry_mixes(
        description='Клеевые составы',
        description2='Для блоков'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Для систем теплоизоляции',
    'для систем теплоизоляции'
]))
async def get_glue_for_thermal_insulation_systems(message: types.Message):
    answer = db.get_dry_mixes(
        description='Клеевые составы',
        description2='Для систем теплоизоляции'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    'Облицовочные',
    'облицовочные'
]))
async def get_facing(message: types.Message):
    answer = db.get_dry_mixes(
        description='Клеевые составы',
        description2='Облицовочные'
    )
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🧱 Кладочные составы',
    'Кладочные составы',
    'кладочные составы'
]))
async def get_masonry_composition(message: types.Message):
    answer = db.get_dry_mixes(description='Кладочные составы')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟨 Короед',
    'Короед',
    'короед'
]))
async def get_koroed(message: types.Message):
    answer = db.get_dry_mixes(description='Короед')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟩 Корник',
    'Корник',
    'корник'
]))
async def get_kornik(message: types.Message):
    answer = db.get_dry_mixes(description='Корник')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟫 Самонивелиры',
    'Самонивелиры',
    'самонивелиры'
]))
async def get_self_leveling(message: types.Message):
    answer = db.get_dry_mixes(description='Самонивелиры')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🔴 Стяжки',
    'Стяжки',
    'стяжки'
]))
async def get_creed_mix(message: types.Message):
    answer = db.get_dry_mixes(description='Стяжки')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '⚪ Цемент',
    'Цемент',
    'цемент'
]))
async def get_cement(message: types.Message):
    answer = db.get_dry_mixes(description='Цемент')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟡 Шпатлевка',
    'Шпатлевка',
    'шпатлевка'
]))
async def get_putty(message: types.Message):
    answer = db.get_dry_mixes(description='Шпатлевка')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟢 Штукатурка',
    'Штукатурка',
    'штукатурка'
]))
async def get_plaster(message: types.Message):
    answer = db.get_dry_mixes(description='Штукатурка')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals=[
    '🟣 Шуба',
    'Шуба',
    'шуба'
]))
async def get_shuba(message: types.Message):
    answer = db.get_dry_mixes(description='Шуба')
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


@dp.message_handler(Text(equals='OSB-плиты влагостойкие'))
async def get_osb(message: types.Message):
    answer = db.get_osb()
    await message.answer(
        text=answer,
        parse_mode='HTML'
    )


ppt_thickness = (1, 2, 3, 4, 5, 7, 8, 10)
ppt_density = (10, 15, 20, 25, 35)
sheet_type = ('А', 'Б')
ppt_calculator_text = f'❗ Для расчета пенопласта введите следующие данные <b>ЧЕРЕЗ ЗАПЯТУЮ</b>:\n\n' \
                      f'<b><code>площадь \м2\, </code></b>' \
                      f'<b><code>толщина листа \см\\ {ppt_thickness}, </code></b>' \
                      f'<b><code>плотность пенопласта {ppt_density}, </code></b>' \
                      f'<b><code>листы без паза или с пазом (А, Б)</code></b>\n\n' \
                      f'<b>ПРИМЕР:</b>\n' \
                      f'<code>15.5, 5, 20, А</code>\n\n' \
                      f'👆 <i>Текст выше можно скопировать в качестве шаблона, нажав на него 👌</i>\n\n' \
                      f'Введите ваши данные 👇'


@dp.message_handler(Text(equals=[
    '✅ Рассчитать пенопласт',
    'Рассчитать пенопласт',
    'рассчитать пенопласт'
]))
async def get_ppt_calculator(message: types.Message):
    await message.answer(
        text=ppt_calculator_text,
        parse_mode='HTML'
    )

    @dp.message_handler()
    async def ppt_calculator(msg: types.Message):
        try:
            data = msg.text.split(',')
            if len(data) != 4 \
                    or int(data[1]) not in ppt_thickness \
                    or int(data[2]) not in ppt_density \
                    or data[3].strip().upper() not in sheet_type:
                raise ValueError
            if int(data[1]) == 1 and (int(data[2]) in (10, 15) or data[3].strip().upper() == 'Б'):
                raise await msg.answer(
                    text='🙁 К сожалению, пенопласт толщиной 1 см\n'
                         'не может быть ниже <b>20</b> плотности\n'
                         'и только <b>листы без паза</b>...',
                    parse_mode='HTML'
                )
            square = float(data[0])
            thickness = int(data[1])
            density = int(data[2])
        except (TypeError, ValueError):
            answer = '❗ НЕКОРРЕКТНЫЙ ВВОД ❗\n' + ppt_calculator_text
            await msg.answer(text=answer, parse_mode='HTML')
        else:
            s_type = data[3].strip().upper()
            # большие листы
            num_of_large_sheets = math.ceil(square)
            # маленькие листы
            num_of_small_sheets = math.ceil(square * 2)
            # объем
            capacity = num_of_small_sheets * 0.5 * (thickness / 100)
            with open('products.json', 'r', encoding='utf8') as f:
                price_per_cubic_metr = json.load(f).get('PPT_PRICE_PER_CUBIC_METER')
                price = round(price_per_cubic_metr[f'ППТ-{density}-{s_type}'] * capacity, 2)
            await msg.answer(
                text=f'<i>Площадь:</i> <b>{square}м2</b>\n'
                     f'<i>Толщина листа:</i> <b>{thickness}см</b>\n'
                     f'<i>Плотность:</i> <b>{density}</b>\n'
                     f'<i>Тип листов:</i> <b>{"Без паза" if s_type == "А" else "С пазом"}</b>\n\n'
                     f'📜 <i>Количество листов:</i>\n'
                     f'<b>{num_of_large_sheets}шт</b> 1000*1000мм\n'
                     f'<i>или</i>\n'
                     f'<b>{num_of_small_sheets}шт</b> 1000*500мм\n\n'
                     f'📦 <i>Объем:</i> <b>{"%.3f" % capacity}м3</b>\n\n'
                     f'💵 <i>Примерная стоимость:</i>\n'
                     f'<b>{"%.2f" % price} руб.</b>\n'
                     f'<i>Примерная стоимость с учетом скидочной карты (3%):</i>\n'
                     f'<b>{"%.2f" % (price - (price * 0.03))} руб.</b>\n\n'
                     f'❗ Наличие листов нужного размера и количества\n'
                     f'уточняйте по телефонам:\n'
                     f'📞 +375297804352 <b>(МТС)</b>\n'
                     f'📞 +375291990505 <b>(A1)</b>\n'
                     f'📞 32-06-06 <b>(Городской)</b>',
                parse_mode='HTML'
            )


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    if not check_permission(message):
        await message.answer('У Вас нет доступа к панели администратора.')
    else:

        await message.answer(text='Yes')

