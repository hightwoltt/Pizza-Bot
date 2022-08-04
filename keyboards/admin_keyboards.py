from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('/Поделиться номером', 
    request_contact=True)
b5 = KeyboardButton('/Моё местоположение', 
    request_location=True)

b_load = KeyboardButton('/Загрузить')
b_delete = KeyboardButton('/Удалить')



button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True)\
    .add(b_load).add(b_delete)

button_case_admin.row(b1, b2).add(b3).row(b4, b5)