from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from create_bot import dp, bot
from keyboards import kb_client


''' ======================== CLIENT PART ======================== '''

async def commands_start(message: types.Message):
    try:
        username = bot.user.first_name
        await bot.send_message(message.from_user.id,  f'Приятного аппетита {username}', \
            reply_markup=kb_client
        )
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, наишите ему:\
            \nhttps//t.me/TODO-BRO-BOT')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, \
        ' Пн-Пт 9:00 - 22:00 \nСб-Вс 9:00 - 02:00',
        )


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, \
        'Восток-2; Дом-5; Кв-27'  
        )


def register_client_handlers(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Адрес'])


    