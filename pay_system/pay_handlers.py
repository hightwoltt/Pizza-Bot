from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType
from aiogram import Dispatcher


from pay_system.pay_messages import MESSAGES
from pay_system.pay_configs import PAYMENTS_TOKEN, items_image
from create_bot import dp, bot

import datetime


PRICES = [
    LabeledPrice(label='Пицца 4 Сыра', amount=4000),
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


@dp.message_handler(commands=['pay_start'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['start'])


@dp.message_handler(commands=['pay_help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])


@dp.message_handler(commands=['terms'])
async def terms_cmd(message: Message):
    await message.answer(MESSAGES['terms'])


@dp.message_handler(commands=['buy'])
async def buy_command(message: Message):
    await bot.send_invoice(message.chat.id,
        title = MESSAGES['title'],
        description = MESSAGES['description'],
        provaider_token = PAYMENTS_TOKEN,
        currency = 'KZT',
        item_img = items_image,
        photo_height = 1920,
        photo_width = 1080,
        photo_size = 1920,
        need_mail = True,
        phone_num = True,
        is_flexible = True,
        prices = PRICES,
        start_parameter = 'example',
        payload = 'some_invoice'
    )


@dp.shipping_query_handler(lambda q: True)
async def shipping_procces(shipping_query: ShippingQuery):
    if shipping_query.shipping_adress.coununtry_code == 'RU':
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


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message : Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.\
            total_amount, currency=message.successful_payment.currency)
    )
    
    
