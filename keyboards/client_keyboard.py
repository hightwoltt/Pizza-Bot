from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Create buttons
b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('/Поделиться номером', 
    request_contact=True)
b5 = KeyboardButton('/Моё местоположение', 
    request_location=True)

kb_client = ReplyKeyboardMarkup(
    resize_keyboard=True,
    )

# Button panel settings
kb_client.row(b1, b2).add(b3).row(b4, b5)