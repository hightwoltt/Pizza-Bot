from aiogram import types, Dispatcher
from aiogram.types import (ReplyKeyboardRemove, ContentType,
                            Message, ShippingOption, 
                            ShippingQuery, LabeledPrice, 
                            PreCheckoutQuery)


from create_bot import dp, bot
from keyboards import kb_client
from data_base import sql_base
from pay_messages import MESSAGES
from pay_configs import PAYMENTS_TOKEN, item_url


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


# Output menu positions
async def pizza_menu_comand(message: types.Message):
    await sql_base.sql_read(message)





# ====================================================== #
# ====================================================== #
# ====================================================== #
# ===================== PAY SYSTEM ===================== #
# ====================================================== #
# ====================================================== #
# ====================================================== #




PRICES = [
    LabeledPrice(label='Пепперони', amount=5000)
]


SPEED_SHIP = ShippingOption(
    id='speed_ship',
    title='Наибыстрейшая доставка'
).add(LabeledPrice('Лично в руки', 7990))


STANDARD_SHIP = ShippingOption(
    id='standard_ship',
    title='Доставка в течении 3х дней'
).add(LabeledPrice('На склад ближайшего магазина', 2490))


PICKUP_SHIP = ShippingOption(
    id='pickup_ship',
    title='В любоой день с 9:00 до 18:00'
).add(LabeledPrice('На складе ближайшего мазазина', 100))


async def terns_command(message: Message):
    await message.answer(MESSAGES['terns'])


async def buy_command(message: Message):
    await bot.send_invoice(message.chat.id,
        title = MESSAGES['item_title'],
        description = MESSAGES['items_description'],
        provider_token=PAYMENTS_TOKEN,
        currency='rub',
        photo_url=item_url,
        photo_height = 620,
        photo_width = 880,
        photo_size = 800,
        need_email=True,
        need_phone_number=True,
        is_flexible=True,
        prices=PRICES,
        start_parameter='example',
        payload='some_invoice'
    )


async def successful_payment(message : Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.\
            total_amount, currency=message.successful_payment.currency)

    )


@dp.shipping_query_handler(lambda q: True)
async def shipping_procces(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.coununtry_code == 'RU':
        return await bot.answer.shipping_query(
        shipping_query.id,
        ok=False,
        error_message=MESSAGES['COUNTRY_ERROR']
    )

    shipping_options = [SPEED_SHIP]

    if shipping_query.shipping_adress.coununtry_code == 'KZ':
        shipping_query.append(STANDARD_SHIP)

        if shipping_query.shipping_adress.sity == 'Караганда':
            shipping_query.append(PICKUP_SHIP)
    
    await bot.answer_shipping_querry(
        shipping_query.id,
        ok=True,
        shipping_options = shipping_options
    )

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_procces(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_querry(pre_checkout_query.id, ok=True)


# Registering commands for a bot (instead of using decorators)
def register_client_handlers(dp : Dispatcher):

    # other handlers
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Адрес'])
    dp.register_message_handler(pizza_menu_comand, commands='Меню')

    # payment handlers
    dp.register_message_handler(terns_command, commands='terns')
    dp.register_message_handler(buy_command, commands='buy')
    dp.register_message_handler(successful_payment, content_types=\
        ContentType.SUCCESSFUL_PAYMENT)
    