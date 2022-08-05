from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os


storage=MemoryStorage()

# Geting from virtual environment bot token and register dispatcher
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

