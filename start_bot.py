from aiogram.utils import executor
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from env_conf import TELEGRAM_BOT_TOKEN


storage = MemoryStorage()
client = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(client, storage=storage)

if __name__ == '__main__':
    executor.start_polling(dp)
