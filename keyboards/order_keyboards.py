from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Еда')
b2 = KeyboardButton('/Напитки')

button_case_order = ReplyKeyboardMarkup(resize_keyboard=True)\
    .row(b1, b2)