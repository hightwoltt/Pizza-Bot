from create_bot import bot, dp

import sqlite3 as sq


# Create a database table
def sql_start():
    global base, cur
    base = sq.connect('3,14zza.db')
    cur = base.cursor()
    
    if base:
        print('\n****** Data base connected ******\n')
    base.execute('CREATE TABLE IF NOT EXISTS classes(eat TEXT,\
    drink, TEXT, combo -> ДОЛЖНА БЫТЬ ССЫЛКА НА ОБЪЕКТЫ БАЗЫ С НЕСКОЛЬКИМИ ПОЗИЦИЯМИ)')

    base.execute('CREATE TABLE IF NOT EXISTS statuses(new_client INTEGER,\
    client INTEGER, premium_client INTEGER)')

    base.execute('CREATE TABLE IF NOT EXISTS order(client INTEGER, order_positions FOREIGN KEY\
        position.id)')

    base.execute('CREATE TABLE IF NOT EXISTS position(photo TEXT, name TEXT, \
        description TEXT, price INTEGER, class FOREING KEY classes.id)')

    base.execute('CREATE TABLE IF NOT EXISTS payment(payment_client FOREING KEY order.id, \
        payment_date DATETIME, payment_order FOREING KEY order.id)')

    base.execute('CREATE TABLE IF NOT EXISTS client(name TEXT, status FOREIGN KEY statuses.id,\
        adress TEXT, phone_number TEXT, payments_history FOREIGN KEY payment.id)')

    base.commit()


# Insert to database command
async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# Full menu output command
async def sql_read(message):
    for position in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )
        

# Drinks menu output command
async def sql_read(message):
    for position in cur.execute('SELECT drinks FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )
        
        
# Eat menu output command
async def sql_read(message):
    for position in cur.execute('SELECT eat FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, position[0],
                f'{position[1]}\n \
                \nОписание: {position[2]}\n \
                \nЦена - {position[3]}'
        )