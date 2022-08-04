from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from create_bot import dp, bot
from keyboards import kb_client
from data_base import sql_base


''' ======================== CLIENT PART ======================== '''

# Bot start command and send message from user
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я бот пиццерии 3.14zza не хочешь посмотреть меню?', \
            reply_markup=kb_client
        )
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, наишите ему: \
            \nhttps//t.me/TODO-BRO-BOT')


# Work schedule output fuction
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, \
        ' Пн-Пт 9:00 - 22:00 \nСб-Вс 9:00 - 02:00',
        )

# Place adress output fuction
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, \
        'Восток-2; Дом-5; Кв-27'  
        )

async def pizza_menu_comand(message: types.Message):
    await sql_base.sql_read(message)

# Register decorators
def register_client_handlers(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Адрес'])
    dp.register_message_handler(pizza_menu_comand, commands='Меню')


    