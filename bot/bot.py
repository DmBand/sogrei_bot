import logging

from aiogram.utils import executor
from create_bot import dp
from handlers import client

client.register_client_handlers(dp)

logging.basicConfig(level=logging.INFO)

executor.start_polling(
    dp,
    skip_updates=True
)
