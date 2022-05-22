import logging
from aiogram import Bot, Dispatcher, executor, types

from token import token

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='test')
async def cmd_test(message: types.Message):
    await message.reply('test')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
