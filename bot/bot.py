from aiogram.utils import executor
from command_handlers import dp

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True
    )