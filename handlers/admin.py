from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from create_bot import dp, bot
from data_base import sql_base
from keyboards import admin_keyboards


''' ======================== ADMIN PART ======================== '''

ID = None

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Signal that admin mode is enabled
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что тебе нужно хозяин?',
        reply_markup=admin_keyboards.button_case_admin)
    await message.delete()

# Start add position
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузите фото')
    
# Cancel position creation
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Операция отменена')

# Load position photo
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь название')

# Load position name
async def load_name(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Добавьте описание')

# Load position description
async def load_description(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Назначьте цену')

# Load position price
async def load_price(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:  
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sql_base.sql_add_command(state)

        await message.answer('Позиция добавленна в меню')
        await state.finish()

# Register decorators
def register_admin_handlers(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='Отмена')
    dp.register_message_handler(cancel_handler, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['Godmode_on'], is_chat_admin=True)


     