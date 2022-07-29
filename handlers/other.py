from aiogram import types, Dispatcher
from create_bot import dp

import json, string
import datetime
import os



''' ======================== GENERAL PART ======================== '''


async def chat_censorship(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('commands/badwords.json')))) != set():
            await message.reply('Маты запрещены!!!')
            await message.delete()


def register_other_hanlers(dp : Dispatcher):
    dp.register_message_handler(chat_censorship)