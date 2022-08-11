help_message = ''' 
Напишите /buy, чтобы перейти к заказу.
Узнать правила можно по команде /terns
Чир-бы ознакомиься с меню /menu
 '''

pre_buy_alert = ''' Счёт для оплаты вашего заказа '''

terns = ''' Правила (добавлю сводку несколько позже) '''

# ======= ПРИДУМАТЬ КАК РЕАЛИЗОВАТЬ ПЕРЕДАЧУ НЕСКОЛЬКИХ ТОВАРОВ СЮДА =======

items_title = ''' Пепперони ''' 

items_description = ''' ПИЦЦА ПИЗДАТАЯ '''

UK_ERR = ''' К сожалению в данную локацию доставку совершить нельзя '''

successful_payment = ''' 
План на сумму {total_amount} {currency} совершён успешно!
'''

MESSAGES = {
    'help' : help_message,
    'pre_buy_alert' : pre_buy_alert,
    'terns' : terns,
    'item_title' : items_title,
    'items_description'  :items_description,
    'COUNTRY_ERROR' : UK_ERR,
    'successful_payment' : successful_payment,
}