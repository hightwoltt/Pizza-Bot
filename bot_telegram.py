from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import string, os, json, datetime

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

dt = datetime.datetime.now()

dt_string_format = dt.strftime("Date %d.%m.%Y time: %H:%M")


''' ======================== CLIENT PART ======================== '''

@dp.message_handler(commands=['start','help'])
async def commands_start(message: types.Message):

    try:
        await bot.send_message(message.from_user.id,  'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, наишите ему:\
            \nhttps//t.me/TODO-BRO-BOT')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    
    await bot.send_message(message.from_user.id, ' Пн-Пт 9:00 - \
        22:00 \nСб-Вс 9:00 - 02:00')


@dp.message_handler(commands=['Адрес'])
async def pizza_place_command(message: types.Message):
    
    await bot.send_message(message.from_user.id, 'Восток-2; Дом-5; Кв-27')



''' ======================== ADMIM PART ======================== '''



''' ======================== GENERAL PART ======================== '''

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('commands/badwords.json')))) != set():
            await message.reply('Маты запрещены!!!')
            await message.delete()





































async def on_startup(_):
    print(f'\nBot started\n\nstatus - Online\ntime statted - {dt_string_format}')

executor.start_polling(
    dp, skip_updates=True,
    on_startup=on_startup
)